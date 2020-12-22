from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Insert url: ")
if len(url) < 1:
    url = "https://www.google.com/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
