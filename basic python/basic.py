print("Hello, World!")

name = "Alice"
age = 25
height = 5.6
is_student = True
print(name, age, height, is_student)



name = input("Enter your name: ")
print("Hello, " + name + "!")



num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")



for i in range(5):
    print(i)


count = 0
while count<5:
    print(count)
    count+=1


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
p = Person("Alice", 25)
print(p.greet())
