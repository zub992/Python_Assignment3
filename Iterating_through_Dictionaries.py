student={"name":"Zubair Akram","age":"19","grade":"A"}  # Dictionary of Student
# This loop is printing the each key
for each_key in student.keys():
    print(each_key) 
print("__________________________")    


print("___________________________") 
# This loop is printing the each Value
for each_value in student.values():
    print(each_value)
print("______________________________")  

for each_key,each_value in student.items():
    print("Key is "+each_key+" Value is "+each_value )   # This loop is for each key-value pair
print("_________________________________________")
for each_key in student.keys():
    if each_key=="grade":
       print("Key is Present")
if each_key!="grade":                                 # This is the code for the Check of key "grade"
    print("Key not found")       
       
   
print("_______________________________")        
count=0
 
for each_key in student.keys():
    count+=1
print("The Number of Keys are :"+str(count))    # This is the code for counting the keys in dictionary
