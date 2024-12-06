query="hello world hello python world"
words=query.split()
count_words={}
for word in words:
    if word in count_words:
        count_words[word]+=1
    else:
        count_words[word]=1
print(count_words)            # this is the code for the counting of the words
 

dict={'a': 10, 'b': 15, 'c': 7}
max_value_in_dict=max(dict,key=dict.get)
print(max_value_in_dict)  # this is the code for key with max value

square_dictionary={i:i**2 for i in range(1,5+1)}  
print(square_dictionary)  # This is the code for mapping square number



dict2={'a': 10, 'b': 15, 'c': 10, 'd': 15}  # This dictionary contain the duplicate
unique_dict={}   # This is the dictionary which will contain the unique
for key,value in dict.items():
    if value not in dict2:
        unique_dict[key]=value
print(unique_dict)        

