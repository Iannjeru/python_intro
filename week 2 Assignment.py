my_list=[]

#Append 
my_list.extend([10,20,30,40])
#Insert
my_list.insert(1,15)

#extend the list
my_list.extend([50,60,70])
#Remove an element
my_list.pop()

#sort the list
my_list.sort()
#find the index of an element
index_of_30=my_list.index(30)
print("Index of 30:", index_of_30)

print("Final List:", my_list)