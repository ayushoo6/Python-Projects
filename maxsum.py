a=map(int,input().split())
b=map(int,input().split())
n=int(input())
p=list(map(float,input().split()))
sum_a=0.0
sum_b=0.0
for i in range(a):
    sum_a += p[i]
for i in range(b):
    sum_b += p[i]
m_a=20*[0]
m_b=20*[]
m_a[0]=sum_a/a
m_b[0]=sum_b/b
j=1
for i in range(a,n):
    j+=1
    sum_a +=(-p[i-a] + p[i])
    m_a[j] = sum_a/a
j=1
for i in range(b,n):
    j+=1
    sum_b +=(-p[i-b] + p[i])
    m_b[j] = sum_b/b
    
ab=0
count=0
if(m_a[b-a] > m_b[0] and ab==0): 
    ab = 1
if(m_a[a-b] < m_b[0]): 
    ab = -1
    
for i in range(1,n-b+1):
    if(m_a[b-a+i] < m_b[i] and ab == 1):
        count += 1
        ab = -1
    elif(m_a[b-a+i] > m_b[i] and ab == -1):
        count += 1
        ab = 1
print(count)
