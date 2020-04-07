import operator
# original list
a_list = [10, 12, 14, 14, 16, 28, 28, 30]
# change the list to a dictionary to get rid of duplicates.Then change it back to a list.
a_list = list(dict.fromkeys(a_list))
print("The list without the duplicates is : ", a_list)
# we sort the list 
a_list.sort(reverse = True)
print("The descending sorted list is : ", a_list)
# the original dictionary
a_dict = {"a":10, "b":12, "c":14, "d":14, "e":16, "f":28, "g":28, "h":30}
x = {}
for key,value in a_dict.items():
  if value not in x.values():
    x[key] = value
a_dict = x
print("the dictionary without the duplicates is : ", a_dict)

sorted_d = dict(sorted(a_dict.items(), key=operator.itemgetter(1),reverse=True))
print("The dictionary is sorted and descending by value : ",sorted_d)