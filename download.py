import urllib.request,urllib.parse
from pathlib import Path
def download(month):
    q={"$select":"unique_key,created_date,closed_date,agency,complaint_type,borough","$where":f"created_date >= '2025-01-01T00:00:00' AND created_date < '2025-02-01T00:00:00' AND borough = 'QUEENS'","$order":"unique_key","$limit":100000}
    url="https://data.cityofnewyork.us/resource/erm2-nwe9.csv?"+urllib.parse.urlencode(q)
    with urllib.request.urlopen(url,timeout=100) as r: data=r.read()
    assert data.startswith(b'"unique_key"') or data.startswith(b'unique_key')
    (Path(__file__).resolve().parent/'data'/'queens-2025-01.csv').write_bytes(data)
if __name__=='__main__':download(1)
