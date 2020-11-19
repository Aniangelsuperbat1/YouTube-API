from googleapiclient.discovery import build

API_KEY = "AIzaSyBvp2BdZow7o9DWssirx_QgZzjFH2--pNw"

service = build("youtube", "v3", developerKey=API_KEY)

request = service.channels().list(
    part='statistics',
    forUsername="Randy Santel"
)
response = request.execute()

print(response)
