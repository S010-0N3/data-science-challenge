s = open("data.csv","r")

name= s.read()
list_names= name.split("\n")
#print(list_names[0:9])

name_data= []

for i in list_names:
  split_list = i.split(",")
  name_data.append(split_list)


numerical_list =[]

for i in name_data:
  change = float(i[1])
  numerical_list.append(change)

#print(numerical_list[0:10])

#print(type(numerical_list[1]))
  

final_list= []

for i in name_data:
  if float(i[1]) > 1000:
    final_list.append(i[0])

print(final_list[0:10])