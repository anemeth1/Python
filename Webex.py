import http.server
import urllib.parse
import json
 
class WebSzerver(http.server.SimpleHTTPRequestHandler):
    gyümölcsök = {
        'alma': 3,
        'banán': 2,
        'narancs': 5,
    }
 
    def do_GET(self):
        elemzett_url = urllib.parse.urlparse(self.path)
        if elemzett_url.path == '/gyumolcsok.html':
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif elemzett_url.path == '/gyumolcs':
            self.válasz()
        else:
            self.send_response(500)
            self.end_headers()
 
    def do_POST(self):
        elemzett_url = urllib.parse.urlparse(self.path)
        if elemzett_url.path == '/gyumolcs':
            kérés = json.loads(self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8'))
            fajta = kérés['fajta']
            darab = int(kérés['darab'])
            if fajta not in self.gyümölcsök:
                self.gyümölcsök[fajta] = 0
            self.gyümölcsök[fajta] += darab
            if self.gyümölcsök[fajta] == 0:
                self.gyümölcsök.pop(fajta)
            self.válasz()
        else:
            self.send_response(500)
            self.end_headers()
 
    def válasz(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(self.gyümölcsök, ensure_ascii=False), 'UTF-8'))
 
http.server.HTTPServer(('localhost', 8080), WebSzerver).serve_forever()

