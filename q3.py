#3. Analogue Image Processing.
import re
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
f="c:/users/aayush/desktop/edgistfy.jpg"
t=pytesseract.image_to_string(Image.open(f))
m=re.search("Tumkur Road",t)
print(m.group(0))
n=re.search(r"AVAILABLE",t)
print(n.group(0))
a=re.search(r"INDUSTRIAL/",t)
print(a.group(0))
b=re.search(r"Warehouse",t)
print(b.group(0))
c=re.search(r"Nelamangala",t)
print(c.group(0))
d=re.search(r"Dobespet. 1 to 100",t)
print(d.group(0))
e=re.search(r"acres. 1000 to",t)
print(e.group(0))
f=re.search(r"1,00,000 saft. NAIK:",t)
print(f.group(0))
g=re.search(r"914",t)
print(g.group(0))
h=re.search(r"1326819",t)
print(h.group(0))
print(m.group(0) +n.group(0) +a.group(0) +b.group(0) +c.group(0) +d.group(0) +e.group(0) +f.group(0) +g.group(0)+h.group(0))
