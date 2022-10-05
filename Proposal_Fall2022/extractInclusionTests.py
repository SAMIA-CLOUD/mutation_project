
delta=0

#read and process mutants killed by tests

def loadTests():
    data={}
    file = open('Subsets.txt')
    lines=file.readlines();
    for i in range(0,len(lines)):
        line=lines[i].strip().split(":");
        test_suite=line[0]
        tests=line[1].split(',');
        data[test_suite]=tests;
    return data;

data= loadTests();

inclusions=[];
for t1 in data:
    for t2 in data:
        if t1==t2:
            continue;
        if(all(x in data[t2] for x in data[t1])):
            inclusions.append('"'+t1+'" -> "'+t2+'"');

writer = open("graph_inclusions_tests.txt",'w');
writer.write("\n".join(inclusions));
writer.close();
