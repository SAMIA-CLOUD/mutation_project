
experiment="Potential"

writer=open(experiment+"_inclusion.txt",'w');


sets={}
inclusion={}
names=[]
file=open(experiment+"Effectivness.txt")
lines=file.readlines()
for line in lines:
	name,l=line.strip().split('": ')
	l=l.split(',')
	l.sort()
	name=name+'"'
	sets[name]=l
	inclusion[name]=[]


for n1 in inclusion:
	for n2 in inclusion:
		if n1==n2:
			continue
		if(all(x in sets[n2] for x in sets[n1])):
			inclusion[n1].append(n2)

for n1 in inclusion:
	for n2 in inclusion[n1]:
		writer.write(n1+" -> "+n2+"\n")
writer.close();