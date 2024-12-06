dict={"person":{"name":"zubair","age":"19"},"Adress":{"Street":"123 Elm St","city":"Boston"}}  # This is the Nested dictionary
city=dict["Adress"]
# print(city["city"])   # This is printing the City value


dict["Adress"]["Phone"]="123-456-7890"  # Key is added inside the nested dictionary


del dict["Adress"]    # Adress Key is deleted


for each_key in dict.keys():    
    print(each_key)  #  This will print only the person key because the Adress key is deleted

