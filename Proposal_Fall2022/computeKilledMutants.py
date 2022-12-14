

dictionary={};
delta=1
file=open('delta.csv');
lines=file.readlines();
for i in range(1,len(lines)):
    line=lines[i].strip().split(",");
    mutant=int(line[0][1:])
    tests=line[delta+1].strip().split(';');
    for t in tests:
        if t not in dictionary:
            dictionary[t]=[];
        dictionary[t].append(mutant)

results={};
file=open('Subsets Used.txt');
lines=file.readlines();
for line in lines:
    line=line.strip().split(":");
    t_name=line[0];
    tests=line[1].split(',');
    results[t_name]=set();
    for t in tests:
        if t not in dictionary:
            continue;
        mutants_killed=dictionary[t];
        for m in mutants_killed:
            results[t_name].add(m)
    temp=sorted(results[t_name])
    temp = ['M'+str(j) for j in temp]
    results[t_name] = temp;

writer = open('mutants_by_Ti'+str(delta)+'.csv','w')
writer.write("Test Suite Subset, Number of Killed Mutants, Mutants\n")
for Ti in results:
    writer.write(Ti+","+str(len(results[Ti]))+","+";".join(results[Ti])+"\n")


writer.close()
