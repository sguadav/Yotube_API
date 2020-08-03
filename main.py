from API_info import api_key
from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(part='statistics', forUsername='schafer5')
response = request.execute()

print(response)


