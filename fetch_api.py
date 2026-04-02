import urllib.request
import json

url = "https://www.datos.gov.co/resource/pare-7x5i.json?$limit=5"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read())
print(json.dumps(data, indent=2))
