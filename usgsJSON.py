
import urllib.request 
import json

def geoResults(data):
    JSON = json.loads(data)
    if "title" in JSON["metadata"]:
        print(JSON["metadata"]["title"])
    
    count = JSON["metadata"]["count"]
    print(count)
    
    for i in JSON["features"]:
        print(i["properties"]["place"])
    print("------------------\n")

    for i in JSON["features"]:
        if i["properties"]["mag"] >= 6.0:
            print(i["properties"]["place"])
    print("------------------\n")
    
    for i in JSON["features"]:
        felt = i["properties"]["felt"]
        if felt != None:
            print(i["properties"]["place"],felt,"times")
  
def main():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson"
    webUrl = urllib.request.urlopen(url)
    data = webUrl.read()
    geoResults(data)

main()
