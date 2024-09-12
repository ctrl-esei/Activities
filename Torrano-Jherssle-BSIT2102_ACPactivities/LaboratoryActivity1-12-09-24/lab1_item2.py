num1, num2 = input("Enter two space-seperated characters: ").split()

print ("-----------------------------------------------")
print ("The Character with greater value is: " + str(max(num1, num2)))
print ("-----------------------------------------------")

print("showing ASCII Values:")

print(num1 + ": " + str(ord(num1)))
print(num2 + ": " + str(ord(num2)))
