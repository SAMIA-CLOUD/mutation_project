def loadMutant(filename):
	file=open('test results/'+filename+'.txt');
	lines=file.readlines();
	data={};
	for line in lines:
		line=line.strip().split(",");
		test=line[0].strip();
		output=line[1].strip();
		data[test]=output;
	return data;

def isError(test_output):
	if ("java.lang" in test_output) or ("error" in test_output):
		return True
	return False

minimal_set_subs=['M1','M19','M23','M24','M25','M27','M44','M45','M48','M51','M60','M74'];

minimal_set_equ=['M1','M2','M7','M8','M11','M13','M19','M21','M22','M23','M24','M25','M27','M28','M44','M45','M46','M48','M49','M50','M51','M52','M53','M55','M56','M57','M60','M63','M74','M92','M93'];



m_s_d0=['M27','M60','M45','M1','M25','M74','M92','M48','M24','M51','M19','M23']
m_s_d1=['M22','M92','M45','M28','M51','M50','M48']
m_s_d2=['M60','M19','M23','M25','M51','M45','M24','M44','M27','M1','M48']

minimal_set=[m_s_d0,m_s_d1,m_s_d2]

experiment=0;
minimal_set=minimal_set[experiment]

def is_different(res1,res2):
	if experiment==0:
		return res1!=res2
	if experiment==1:
		if isError(res1) or isError(res2):
			return False
		return res1!=res2
	if experiment==2:
		if isError(res1) and isError(res2):
			return False
		return res1!=res2

base_results=loadMutant('Base'); #load the results of the base program

results={};
for m in minimal_set:
	results[m]=loadMutant(m); #load the results of each mutant (test number: test outcome)

dif_set={};
for t in base_results:
	dif_set[t]={};
	for m in minimal_set:
		dif_set[t][m]='0'; #by default the t is not a dif for m
		if is_different(results[m][t],base_results[t]):
		#if t have different results for m and base program, add t to dif set of m
			dif_set[t][m]='1';




writer=open("difsets_"+str(experiment)+".csv","w");
writer.write(","+",".join(minimal_set)+"\n");
for t in dif_set:
	temp=[str(t)];
	for m in minimal_set:
		temp.append(dif_set[t][m]);
	writer.write(",".join(temp)+"\n");
writer.close();


