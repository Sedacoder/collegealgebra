print("My name is Sean")
family = ["Sammy" , "Sean" , "Suzanne" , "Ethan" , "Avery" , "Arthur"]
print(family)
print(family[2])
family = {
    "Father" :{
        "Name" : "Sammy Kibutu",
        "Age" : 36
    },
    "Mother" : {
        "Name": "Suzanne Waweru",
        "Age": 44
    },
    "Child 1" :{
        "Name":"Sean Waweru",
        "Age":16
    },
    "Child 2" :{
        "Name" : "Ethan Kibutu",
        "Age" : 11
    }
}
print(family)
family.update({"Child 3" :{"Name" : "Avery Irungu" , "Age" :3},"Child 4" :{"Name" : "Arthur Maina" , "Age" : 3}})
print(family)

import json

x = json.dumps(family)
print(type(x))
print(x)
car = '{"Brand" : "Audi" , "Model" : "Q8" , "year" : 2019}'
print(type(car))
print(car)
y = json.loads(car)
print(type(y))
print(y)
 
def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    else:
        return sum(numbers) / len(numbers)
    
sample =[84,48,48,38,2,374,47]
print(round(calculate_average(sample),0))

p = lambda a : a*a
print(p(5))
list = [2,3,5,7]
for i in list:
    x = lambda l : l * l
    print(x(5))

def greet_person(name):
    print("Hello " + name)

greet_person("Sean")

def tripler(num):
    return pow(num , 3)

x = map(tripler, [1,4,6,8])
print(x)

for i in 'PYTHON':
    if i in 'AEIOU':
        print(i)

multiplesOfThree = [3,6,9,12,15]
i = 1
while i > 2:
    print(i)
    i += 1











