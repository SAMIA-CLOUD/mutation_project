import copy
def loadMaps():
	file=open('test.txt');
	lines=file.readlines();
	maps={}
	for l in lines:
		l=l.strip().split("\t");
		old=l[0]
		new=l[1]
		if old not in maps:
			maps[old]=[]
		maps[old].append(new)
	return maps;

def NewMutant(mutant,map):
	file=open(mutant+".txt");
	lines=file.readlines();
	writer=open('new/'+mutant+".txt","w");
	for l in lines:
		l=l.strip().split(",");
		old=l[0]
		res=l[1]
		print(mutant,old,map[old])
		new=map[old].pop(0);
		writer.write(str(new)+","+res+"\n");
	writer.close();

total=94
mutants=['M'+str(i) for i in range(1,total+1)];
mutants.append('base');
mapping=loadMaps();
for m in mutants:
	print(m)
	new_map=mapping.copy()
	NewMutant(m,copy.deepcopy(mapping))