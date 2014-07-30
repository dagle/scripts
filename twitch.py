#!/usr/bin/env python
import sys
import urllib
import urllib.request
import simplejson as json
response = urllib.request.urlopen('https://api.twitch.tv/kraken/streams/' + sys.argv[1])
html = response.read().decode("utf-8")
j = json.loads(html)
if len(sys.argv) == 3:
    quality = sys.argv[2]
else:
    quality = 'medium'
if j['stream']:
    print('livestreamer -p mpv ' + j['stream']['channel']['url'] + ' ' + quality)
else:
    print('#Offline')
