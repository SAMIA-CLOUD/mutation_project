#Detla_2


def loadMutant(filename):
	file=open('Specifications/'+filename+'.txt');
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

def is_different_delta2(base_res,R_res,partial):
		if partial==True:
			if isError(base_res) or isError(R_res):
				return False
		else:
			if isError(R_res):
				return False
		return base_res!=R_res



def getDetector(base,R,partial):
	detectors=[]
	for t in R:
		if is_different_delta2(base[t],R[t],partial):
			detectors.append(t); #if t(P)!=t(R) or if P or R diverge (not both)
	return detectors



experiments=["u1","u2","u3"]

data_mu={}
data_mu['u1']={'union':[1,12,16,2,20,21,22,23,25,26,27,31,32,36,37,7,8],'intersection':[12,16,20,21,22,8]}
data_mu['u2']={'union':[1,12,16,2,20,21,22,25,26,31,32,36,37,8],'intersection':[12,16,20,21,22,8]}
data_mu['u3']={'union':[1,12,16,2,20,21,22,23,25,26,27,31,32,36,37,7,8],'intersection':[12,16,20,21,22,8]}

Rs=['R1','R2','R3']
Rs.sort()
S=[str(i) for i in range(1,38)];
assured={}
potential={}
writer_assured=open("AssuredEffectivness.txt","w")
writer_potential=open("PotentialEffectivness.txt","w")

count=1
base=loadMutant('Base'); #load the results of the base program
for experiment in experiments:
	union_theta=[str(i) for i in data_mu[experiment]['union']]
	intersection_theta=[str(i) for i in data_mu[experiment]['intersection']]
	for m in Rs:
		R=loadMutant(m)
		detectors=getDetector(base,R,True);
		detectors_complement=list(filter(lambda t: t not in detectors, S))
		assured_partial=set(t for t in intersection_theta+detectors_complement)
		potential_partial=set(t for t in union_theta+detectors_complement)
	
		detectors=getDetector(base,R,False);
		detectors_complement=list(filter(lambda t: t not in detectors, S))
		assured_total=set(t for t in intersection_theta+detectors_complement)
		potential_total=set(t for t in union_theta+detectors_complement)
		
		
		assured['S'+str(count)+": AssuredEffectivness{"+m+",P}^Total("+experiment+")"]=assured_total
		assured['S'+str(count+1)+": AssuredEffectivness{"+m+",P}^Partial("+experiment+")"]=assured_partial
		
		potential['S'+str(count)+": PotentialEffectivness{"+m+",P}^Total("+experiment+")"]=potential_total
		potential['S'+str(count)+": PotentialEffectivness{"+m+",P}^Partial("+experiment+")"]=potential_partial
		count=count+2

for s in assured:
	writer_assured.write('"'+s+'": '+",".join(assured[s])+"\n")

for s in potential:
	writer_potential.write('"'+s+'": '+",".join(potential[s])+"\n")

writer_assured.close()
writer_potential.close()


