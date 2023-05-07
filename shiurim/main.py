#!/usr/bin/python

import argparse
import requests



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyCTc53Pf0cdgGPS39hAdm_ZQoRTOnQSlHA'

def download_shiur(options):
    res = requests.get(options.url, params={
    'part': 'snippet',
    'q': options.q,
    'maxResults': options.max_results,
    'key': DEVELOPER_KEY
  })
  
    for item in res.json()["items"]:
       if item["id"]["kind"] == "youtube#video":
          print(item)
          return


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='RavAsherWeiss')
  parser.add_argument("--url", help="URL to download from", default="https://youtube.googleapis.com/youtube/v3/search")
  parser.add_argument('--max-results', help='Max results', default=50)
  args = parser.parse_args()

  download_shiur(args)