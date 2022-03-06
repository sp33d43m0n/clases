# month_baby = {'name' : 'samara', 'month' : 4, 'weight[grm]' : 6500, 'height[cms]' : 60.5, 'cirugies': False}
# print(month_baby)
# month_baby.pop('month')
# month_baby['clothes'] = ['colombian', 'american']
# print(month_baby)
# print(month_baby['name'])

# # my_list = ["abc", 123, "xyz"]
# # for i in range(0, len(my_list), 2):
# #     print(i, my_list[i])

# my_list = ["abc", 123, "xyz"]    
# for v in my_list:
#     print(v)

# my_dict = { "name": "Noelle", "language": "Python" }
# for k in my_dict:
#     print(my_dict[k])
#     print(k)
    
month_baby = {'name' : 'samara', 'month' : 4, 'weight[grm]' : 6500, 'height[cms]' : 60.5, 'cirugies': False}   
# for key in month_baby.keys(): #el orden de la lista
# for key in month_baby.values(): # el orden de los valores del diccionario
#     print(key)
    
for key, val in month_baby.items():  #keys , values, items
     print(key, " = ", val)    