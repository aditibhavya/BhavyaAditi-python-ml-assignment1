#taking string and writing in text file
str = input("Enter the text you want to write : ")
file = open("file1.txt","w")
file.write(str)
print("The text that was written in file : ",str)
