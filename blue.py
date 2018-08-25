from bluetooth import *
import requests
nearby_devices = discover_devices(lookup_names = True)
print(nearby_devices)
dev = "" #add device mac address
for name, addr in nearby_devices:
    if dev == name:
        r = requests.post('http://127.0.0.1:5000/track/athome', json={"name": name,"addr": addr})
        r.status_code
        print (r.content)
    

