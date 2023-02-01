#hard coded example
# first = 10.1
# second = 20

# print(float(first)+int(second))

#float takes in decimals where integer will not. 

first = input("first: ")
second = input("second: ")

total = float(first) + float(second)

print(total)
#type conversion for str used here as concat with string and int does not work in python.
print('Sum:' + str(total))
