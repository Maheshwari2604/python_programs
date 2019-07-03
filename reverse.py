def reverse(a): 
  str = "" 
  for i in a: 
    str = i + str
  return str
  
a = "shivam"
  
print ("string  is : ",end="") 
print (a) 
  
print ("reversed string is: ",end="") 
print (reverse(a)) 
