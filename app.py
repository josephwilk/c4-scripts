import requests
import pandas as pd
import json
import sys

# Url you want to search for
url="looneytunes.fandom.com/"
url="josephwilk.net/"
url=sys.argv[1] or url
# Indexes you want to search
index_list = ["CC-MAIN-2024-51-index"]

# store the records
record_list=[]

for index in index_list:
        
 print("[*] Trying index %s" % index)
        
 cc_url  = "http://index.commoncrawl.org/%s?" % index
 cc_url += "url=%s&matchType=domain&output=json" % url
        
 response = requests.get(cc_url)
        
 if response.status_code == 200:
            
    records = response.content.splitlines()
    print(records)
    for record in records:
        record_list.append(json.loads(record))
            
    print("[*] Added %d results." % len(records))
            
    
print("[*] Found a total of %d hits." % len(record_list))

df = pd.DataFrame.from_dict(record_list)
print(df)
