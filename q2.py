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
