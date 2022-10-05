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

minimal_set_subs=['m1', 'm19', 'm23', 'm24', 'm25', 'm27', 'm44', 'm45', 'm48', 'm51', 'm60'];

minimal_set_equ=['m1','m2','m3','m7','m11','m13','m15','m19','m21','m22','m23','m24','m25','m27','m28','m44','m45','m46','m48','m49','m50','m51','m52','m53','m55','m56','m57','m60','m63','m92','m93'];

experiment='Equivalence';

minimal_set=[];
if experiment=='Subsumption':
    minimal_set=minimal_set_subs;
else:
    minimal_set=minimal_set_equ


base_results=loadMutant('Base'); #load the results of the base program

results={};
for m in minimal_set:
    results[m]=loadMutant(m); #load the results of each mutant (test number: test outcome)

dif_set={};
for t in base_results:
    dif_set[t]={};
    for m in minimal_set:
        dif_set[t][m]='0'; #by default the t is not a dif for m
        if results[m][t]!=base_results[t]: #if t have different results for m and base program, add t to dif set of m
            dif_set[t][m]='1';




writer=open("difsets_"+experiment+".csv","w");
writer.write(","+",".join(minimal_set)+"\n");
for t in dif_set:
    temp=[str(t)];
    for m in minimal_set:
        temp.append(dif_set[t][m]);
    writer.write(",".join(temp)+"\n");
writer.close();


