file=open("gep.txt","r")

file_data=[]

for i in file: 
    if(i[-1=="\n"]):
        file_data.append(i[:-1].split("\t"))
    else:
        file_data.append(i.split("\t"))

del file_data [0]


for i in range(len(file_data)):
    csere=''
    for j in range(len(file_data[i][1])):
        if file_data[i][1][j]==',':
            csere+='.'
        else:
            csere+=file_data[i][1][j]
    file_data[i][1]=float(csere)

print(file_data)
print("Készülékek száma:",len(file_data))

mer=0
Mdb=0

for i in range(len(file_data)):
    mer+=int(file_data[i][3])
    Mdb+=1

print("Merevlemez méreteinek átlaga: ",round(mer/Mdb,2))

kereses=1000
nincs=0

for i in range(len(file_data)):
    if(kereses == file_data[i][3]):
        print(file_data[i][0]+"\t"+str(file_data[i][1])+"\t"+file_data[i][2]+"\t"+file_data[i][3]+"\n")
    else:
        nincs+=1


if nincs==len(file_data):
    print("Nincs 1TB-s merevlemez!")

nagy=0
for i in range(len(file_data)):
    if nagy < file_data[i][1]:
        nagy = file_data[i][1]

print("Legnagyobb kijelzőméret:",nagy)