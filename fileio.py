f=open("sample.txt","r")
print(f.read())

f1=open("sample1.txt","w")
f1.write("This is a sample text file")
f1.close()
f1=open("sample1.txt","r")
print(f1.read())

