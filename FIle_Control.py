file=open("spider.txt")
#read one line then transfer power to the next line
print(file.readline())
#read till end of the file
print(file.read())
file.close()#nessary bit

with open("spider.txt") as file:
  print(file.readline())
  
#withcloses the file after the function work is over !

with open("spider.txt") as file:
  for line in file:
      print(line.strip().upper())
      
with open("spider.txt","w") as file:
  file.write("Hello")
  #rewriteseverything
