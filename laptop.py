file=open("gep.txt","r")

file_data=[]

for i in file: 
    if(i[-1=="\n"]):
        file_data.append(i[:-1].split("\t"))
    else:
        file_data.append(i.split("\t"))

del file_data [0]


















