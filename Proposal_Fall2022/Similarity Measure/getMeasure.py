

def loadEdges(filename):
    file=open(filename)
    lines=file.readlines();
    data=[];
    for l in lines:
        data.append(l.strip())
    return data;


#base=loadEdges('mutants_killed_delta1.txt');

others=['pcM25','pcM50','tcM25','tcM50']

writer=open("resultsALL.txt","w")
for o1 in others:
    for o2 in others:
        g1 = loadEdges(o1+'.txt');
        g2 = loadEdges(o2+'.txt');
    
        writer.write("Measure between base "+o1+" and "+o2+" \n")
        union = set(g1+g2)
        intersection = [value for value in g1 if value in g2]
        writer.write("Cardinality of union: "+str(len(union))+"\n")
        writer.write("Cardinality of intersection: "+str(len(intersection))+"\n")
        writer.write("Similarity Measure: "+str(len(intersection)/len(union))+"\n\n\n\n")

writer.close()