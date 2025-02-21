
import requests
import pdb
import time
from pprint import pprint
query = "What is the airspeed velocity of an unladen swallow?"
query = "Thomas%20Lyon-Bowes,%20Lord%20Glamis,%20father,%20John%20Lyon-Bowes,%207th%20Earl%20of%20Strathmore%20and%20Kinghorne"
k = 10
url = f"http://localhost:8893/api/search?query={query}&k={k}"
start_time = time.time()
response = requests.get(url)
print(response)
response = response.json()
delay = time.time() - start_time
pprint(response)
print(f"Time taken: {delay:.3f} seconds")
