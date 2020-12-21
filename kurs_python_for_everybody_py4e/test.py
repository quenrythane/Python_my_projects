import  urllib.request, urllib.parse, urllib. error
from bs4 import BeautifulSoup

url = input("Enter - ")
if len(url) < 1: url = "http://www.dr-chuck.com/page1.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    print(tag.get("href", None))

# http://www.dr-chuck.com/page1.html