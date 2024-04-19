# For loop
numbers = []

for i in range(1, 6):
    numbers.append(i*10)

print(numbers)

#For list comprehension
lista = [i*10 for i in range(1, 6)]
print(lista)

#List comprehension with Lambda function
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
print(numbers)

