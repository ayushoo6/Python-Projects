a=int(input())
s=input()
i=0
a1=0
a2=0
j=0
while(s[j]!="\0"):
    if s[j]=="A":
        a1+=1
    elif s[j]=="B":
        a2+=1
        j+=1
while(s[i]=="-"):
    i+=1
if s[i]=="A":
    a1+=i
start=i
for i in a:
    while(s[i]=='-' and i<f):
        i+=1
    if i==a:
        break
    if s[i]=="A":
        if start==i:
            i+=1
            continue
        a1=a1+(i-start-1)
        start=i
        i+=1
        continue
    start=i
    i+=1
    while(s[i]=="-" and i<f):
        i+=1
    if i==f:
        a2=a2+(i-start-1)
    else:
        if(s[i]=="A"):
            a1=a1+(i-start-1)/2
            a2=a2+(i-start-1)/2
            start=i
            i+=1
        else:
            a2=a2+(i-start-1)
if(a1>a2):
    print("A")
elif(a1==a2):
    print("Government Coalition")
else:
    print("B")
       
    
