from PyPDF2 import PdfFileReader
import pandas as pd
import requests
import json

url = "https://pdf.hres.ca/dpd_pm/"
fulldata = []

df = pd.read_csv('PMs.csv', dtype=str)

for row in df.pm_num:
        r = requests.get(url+row+'.PDF')
        if r.status_code ==200:
                print("PM {} found!".format(row))
                with open('file.pdf', 'wb') as temp:
                        temp.write(r.content)
                        print("downloading temporary file...")
                try:
                        with open('file.pdf', 'rb') as f:
                                p = PdfFileReader(f)
                                bookmark_data={row:p.outlines}
                                fulldata.append(bookmark_data)
                                print("PM {} bookmark extracted".format(row))
                except Exception as e:
                        with open('error.log','a') as log:
                                log.write("Error on PM {}. {} {}\n".format(row,type(e),e.args))
with open('pm_bookmark.json', 'a') as data:
        data.write(fulldata)
print("All bookmarks extracted.")
