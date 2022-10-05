'''
Rules: We need 20 subsets T1 to T20
T1-T5: 32 random
T6-T10: 27 random
T11-15: 22 random
T16-T20: 36 random
'''

import random
T=[i for i in range(1,38)]

subsets=[]

#T1 to T5
t=0;
while t<5:
    temp=list(T)
    for r in range(0,5):
        element_to_remove = random.choice(temp);
        temp.remove(element_to_remove)
    if temp not in subsets:
        subsets.append(temp)
        t+=1;

#T6-T10
t=0;
while t<5:
    temp=list(T)
    for r in range(0,10):
        element_to_remove = random.choice(temp);
        temp.remove(element_to_remove)
    if temp not in subsets:
        subsets.append(temp)
        t+=1;

#T11-T15
t=0;
while t<5:
    temp=list(T)
    for r in range(0,15):
        element_to_remove = random.choice(temp);
        temp.remove(element_to_remove)
    if temp not in subsets:
        subsets.append(temp)
        t+=1;

#T16-T20
t=0;
while t<5:
    temp=list(T)
    for r in range(0,1):
        element_to_remove = random.choice(temp);
        temp.remove(element_to_remove)
    if temp not in subsets:
        subsets.append(temp)
        t+=1;

writer=open("Subsets.txt","w")
for i in range(0,len(subsets)):
    name='T'+str(i+1);
    l=[str(j) for j in subsets[i]]
    writer.write(name+":"+",".join(l)+"\n")



writer.close()