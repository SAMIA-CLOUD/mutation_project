



def loadMutant(filename):
	file=open('test results/'+filename+'.txt');
	lines=file.readlines();
	data={};
	for line in lines:
		line=line.strip().split(",");
		test=line[0].strip();
		output=line[1].strip();
		data[test]=output;
	count=len(data);
	if count!=34:
		print(filename,count);
	return data;

def isSame(res_a,res_b):
	for t in res_a:
		if res_a[t]!=res_b[t]:
			return False;
	return True;

def isError(test_output):
	if ("java.lang" in test_output) or ("error" in test_output):
		return True
	return False
base_results=loadMutant('Base'); #load the results of the base program

mutants=['M1','M2','M7','M8','M11','M13','M19','M21','M22','M23','M24','M25','M27','M28','M44','M45','M46','M48','M49','M50','M51','M52','M53','M55','M56','M57','M60','M63','M74','M92','M93'];

results={};
for m in mutants:
	results[m]=loadMutant(m); #load the results of each mutant (test number: test outcome)

d1={};
d2={};
d0={};
for m in mutants:
	d1[m]=[];
	d2[m]=[];
	d0[m]=[];
	for t in results[m]:
		#for d0, we assume error is an output and we compare strings
		if results[m][t]!=base_results[t]: 
			d0[m].append(t)
		if not(isError(results[m][t]) and isError(base_results[t])):
			if not isError(results[m][t]) and  not isError(base_results[t]):
				if results[m][t]!=base_results[t]: 
					d1[m].append(t);
					d2[m].append(t);
			else:
					d2[m].append(t);

writer=open("delta_analysis.csv",'w');
writer.write("Mutants,Delta 0,Delta 1,Delta 2\n");
for m in mutants:
	if len(d0[m])==0:
		d0[m]=["Empty"];
	if len(d1[m])==0:
		d1[m]=["Empty"];
	if len(d2[m])==0:
		d2[m]=["Empty"];
	tmp=[m,";".join(d0[m]),";".join(d1[m]),";".join(d2[m]),"\n"];
	writer.write(",".join(tmp));
writer.close();