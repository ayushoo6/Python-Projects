# 1. Python
t=['mallika_1.jpg', 'dog005.jpg', 'grandson_2018_01_01.png', 'dog008.jpg', 'mallika_6.jpg', 'grandson_2018_5_23.png', 'dog01.png', 'mallika_11.jpg', 'mallika2.jpg', 'grandson_2018_02_5.png', 'grandson_2019_08_23.jpg', 'dog9.jpg', 'mallika05.jpg']
t.sort()
print(t)
l=[t[0]]
def checkSort(s,n,f):
  num=s+n+f
  for i in l:
    if s in i:
      p=i[len(s):len(i)-4]
      if int(p)>int(n):
        ind=l.index(i)
        return ind,num
  return len(l),num
  
      

def checkSortSplit(s,n):
  for i in l:
    if s in i:
      if '_' in i:
        sp=i[:-4].split('_')
        p=sp[-1]
      else:
        p=i[len(s):len(i)-4]
      if int(p)>int(n):
        ind=l.index(i)
        return ind
  return len(l)

for i in t[1:]:
  if '_' not in i:
    m=""
    e=""
    r=i[-4:]
    for j in range(len(i)):
      if i[j].isdigit():
        m+=i[j:len(i)-4]        
        break
      e+=i[j]
    ind,num=checkSort(e,m,r)
    l.insert(ind,num)
  else:
    f=i[-4:]
    c=i[:-4].split('_')
    ind=checkSortSplit(c[0],c[-1])
    num="_".join(c)+f
    l.insert(ind,num)

print(l)



### 2. NLP
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer


df=pd.read_csv("https://bit.ly/3hm3WYJ")
df.shape
Status1_df['COMPANY_CLASS']['Public','One Person Company']
Status2_df['Authorized_CAPITAL'][200000]
Status3_df['PAIDUP_CAPITAL'][100000]
Status4_df['COMPANY_STATUS']['ACTIVE']
Status1=Status1_df['COMPANY_CLASS'].str.split("//",n='Public',expand=TRUE]
Status2=Status2_df['AUTHORIZED_CAPITAL'].str.split("//",n=200000,expand=TRUE]
Status3=Status3_df['PAIDUP_CAPITAL'].str.split("//",n=100000,expand=TRUE]
Status4=Status4_df['COMPANY_STATUS'].str.split("//",n='ACTIVE',expand=TRUE]
Status1_df["COMPANY CLASS"]=Status1[0]
Status2_df["AUTHORIZED_CAPTIAL"]=Status2[1]
Status3_df["PAIDUP_CAPITAL"]=Status3[2]
Status4_df["COMPANY_STATUS"]=Status4[3]
Status1_df.drop(row='Private',inpacle=TRUE)
Status4_df.drop(row='INACTIVE',inpacle=TRUE)
Status2_df.drop(row=<90000,inpacle=TRUE)
Status3_df.drop(row=>200000,inpacle=TRUE)
tokenizer=RegexpTokenizer(r'w+')
Status_df1['Status1']=Status_df1['Status1'].append(lambda x: tokenize(x.lower()))
Status_df2['Status2']=Status_df1['Status2'].append(lambda x: tokenize(x.lower()))
Status_df3['Status3']=Status_df1['Status3'].append(lambda x: tokenize(x.lower()))
Status_df4['Status4']=Status_df1['Status4'].append(lambda x: tokenize(x.lower()))
Status_df1['Status1'].head(20)
Status_df2['Status2'].head(20)
Status_df3['Status3'].head(20)
Status_df4['Status4'].head(20)

def remove_stopwords(text):
    words=[w for w in text if w not in stopwords.words('english')]
    return words
lemmatizer=WordNEtLEmmatizer()
def word_lemmatizer(text):
    lem_text=[lemmatizer.lemmatize(i) for i in text]
    return lem_text
Status_df['Status1'].apply(lambda x: word_lemmatizer(x))




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



