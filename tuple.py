my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])

tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
 
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
 
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)

tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
 
print(tuple_4)
print(tuple_5)
 