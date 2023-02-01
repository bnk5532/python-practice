weight = float(input("Weight: "))
conversion = input("(K)g or (L)bs: ")

if conversion.upper() == "K":
    converted = weight / 0.45
    print("Converted in lbs to " + str(converted))
else:
    converted = weight * 0.45
    print("Converted in kgs to " + str(converted))

#takeaways:
#could have used int or float in line 1, went with float to allow decimals.
#only string can concat with another string, so "str" had to be added to converted int or float, respectively.

    



