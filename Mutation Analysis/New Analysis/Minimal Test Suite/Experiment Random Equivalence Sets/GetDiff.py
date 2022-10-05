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

minimal_set_equ1=['M19','M21','M22','M23','M24','M25','M27','M28','M44','M45','M46','M48','M49','M50','M51','M52','M53','M55','M56','M57','M60','M63','M74','M92','M93'];

minimal_set_equ2=['M1','M2','M7','M8','M11','M13'];

experiment='Equivalence1';

minimal_set=[];
if experiment=='Equivalence1':
    minimal_set=minimal_set_equ1;
else:
    minimal_set=minimal_set_equ2


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


