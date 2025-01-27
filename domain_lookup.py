import requests
import pandas as pd
import json
import sys
import time

# Url you want to search for
url="looneytunes.fandom.com/"
url="josephwilk.net/"
#url= sys.argv[1]

urls=["WEEPPEND.XYZ",
      "NETWORKSUNION.ORG",
      "QLW.IO",
      "DRAMAHOOD.COM",
      "MOVIEMINT.COM",
      "SUTYENTAKIMI.COM",
      "PLAYFUL11.COM",
      "SIEBOB.INFO",
      "ISTANBULMOBILMASAJ24.COM",
      "MUNDOBASHAJEANS.COM",
      "STOREGEME.COM",
      "5ANONOVOPG.COM",
      "TRADEBULL.INFO",
      "IROOT.COM",
      "THEAIJOBBOARD.COM",
      "ANTOJITOSLINDAMARAZ.COM",
      "IN777A.COM",
      "SANCHEZWELDING.CO",
      "STARKUILLOTTERY.COM",
      "MMAV.ME"
]


url_data = pd.read_csv('export_example_22_01_2025.csv', sep='\t')
urls = ( [r[0].lower() for r in url_data.values])

urls = [ "overresume.co"]

print(urls)

# Indexes you want to search
index_list = ["CC-MAIN-2024-51-index"]

# store the records
record_list=[]

domain_hits = []

for url in urls:
    time.sleep(5)
    
    for index in index_list:
    
        print("[*] Trying index %s" % index)
 
        cc_url  = "http://index.commoncrawl.org/%s?" % index
        cc_url += "url=%s&matchType=domain&output=json" % url
        response = requests.get(cc_url)
 
        if response.status_code == 200:
            records = response.content.splitlines()
            print(records)
            domain_hits.append({url: len(records)})
            for record in records:
                record_list.append(json.loads(record))
                print("[*] Added %d results." % len(records))
    

print(domain_hits)
#print("[*] Found a total of %d hits." % len(record_list))

#df = pd.DataFrame.from_dict(record_list)
#print(df.to_string(max_rows=2000))
