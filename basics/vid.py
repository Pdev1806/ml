# var = "a" , "b" , "c"
# type(var)
# print(type(var))

my_list = [1, 2, 3, "mixed", True]
my_list.append(4)  # Add to end
my_list.insert(0, "apple")  # Insert at index
my_list.remove(3)  # Remove first occurrence
my_list.pop()  # Remove and return last item
my_list[3]  # Access by index
my_list[1:3]  # Slicing [start:end]
my_list[::-1]  # Reverse
len(my_list)  # Length


# for list use []
# rev a list using [::-1]
# to get an index in a list just put ['the index']
# to insert in a list use [a,b] where a is the index and b is the data to be inserted 
# splicing ke liye use [a,b] returns elements from index a to b-1
# .remove(x) removes first occurance of x
# .pop removes last element


# for tuple just put = and write the elements in "" seperated by comma
# or for tuple put it in ()
# eg of tuple 
whatever = "a" , "b"
print(type(whatever))

# for dictionary put elements in {} BUT  each element is a key value pair
# access is by key not index
# eg of dictionary 
whatever2 = {"name" : "Pranav" , "mobile":"24"}
print(type(whatever2))
print(whatever2)


# for set use {} but no key value pairs
# eg of set 
whatever3 = {1,2,3}
print(type(whatever3))


# LIST -> ordered, mutable
# TUPLE -> ordered, immutable
# DICT -> key value pairs, mutable


