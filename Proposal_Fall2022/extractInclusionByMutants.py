
delta=1

#read and process mutants killed by tests

def loadTests():
    data={}
    file = open('mutants_by_Ti'+str(delta)+'.csv')
    lines=file.readlines();
    for i in range(1,len(lines)):
        line=lines[i].strip().split(",");
        test_name=line[0]
        mutants=line[2].split(';');
        data[test_name]=mutants;
    return data;

tests = loadTests();

inclusions=[];
for t1 in tests:
    for t2 in tests:
        if t1==t2:
            continue;
        if(all(x in tests[t2] for x in tests[t1])):
            inclusions.append('"'+t1+'" -> "'+t2+'"');

writer = open("graph_"+str(delta)+".txt",'w');
writer.write("\n".join(inclusions));
writer.close();
