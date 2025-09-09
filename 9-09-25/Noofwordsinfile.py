fp=open("sample.txt","r")
data=fp.read()
words=data.split(" ")
print("No of words in file:",len(words))