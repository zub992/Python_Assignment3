dict1 = {'a': 5, 'b': 10}   
dict2 = {'a': 5, 'b': 7}
result_dict={}
for key in dict1.keys() & dict2.keys():
    if dict1[key]==dict2[key]:
        result_dict[key]=dict1[key]+dict2[key]

        
print(result_dict)   # This is the code for adding the keys if they match

for number in range(1,5):
    n=int(input("Enter the number :"))
    dict={n:n**3}
    print(dict)    # This is the coder which take the input the n positive integes and print cube of 
    # values
