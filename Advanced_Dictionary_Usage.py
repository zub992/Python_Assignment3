dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4} 
merge_dict_1_and_dict2= dict1 | dict2    # This is the code for the Merging the Dictionary
print(merge_dict_1_and_dict2)


list=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
dictionary=dict(list)   # Use the method dict
print(dictionary)           # This is the coder for the convert the list of tuples in the dictionary 



dict={'z': 7, 'a': 2, 'c': 3}
sorted_dict=sorted(dict.keys())  # here is the sorted method is used for the sorting
print(sorted_dict)


dictionary={'a': 1, 'b': 2, 'c': 3}
reverse_dictionary={value:key for key,value in dictionary.items()}
print(reverse_dictionary)
