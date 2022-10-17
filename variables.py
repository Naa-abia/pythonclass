Name = "Abia"
Age = 36
Stipend = 600
FullName = "Abi"
full_name = "Ahmed"
gender = "M"

# Comparison operators

if Name == full_name :
    print("the names are the same")

if Name != FullName :
    print ("the names are not the same")

 #Lgical operators 

if (full_name == "Ahmed" and gender == "M") :
    print("TRUE")

if (FullName == "Abi" or gender == "M") :
    print ("TRUE-OR")   


print(f"Hello {Name}! Your age is {Age}")
# print(f"Hello" + Name + "! Your age is" + Age") - concatination of strings because of the operator(+)
# print("Hello" + Name + "! Your age is" + str(Age)) - x str used to cast an integer to string