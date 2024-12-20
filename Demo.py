
import requests

apiUrl = 'https://webexapis.com/v1/rooms'

access_token = 'ZjBlNjk3OTYtZmNhMS00ODFhLTkxYzEtNGU5OTY4YjNkOTFlNmViYzU1NmQtMWE4_PF84_602d7d50-4ed5-40fc-a8ad-63646501cd00'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }

queryParams = { 'sortBy': 'lastactivity', 'max': '1', 'id':'', 'title':'401' }

response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )

print( response.status_code )
print( response.text )

