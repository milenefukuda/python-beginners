users = ['Milene', 'Dave', 'John']

data = ['Milene', 42, True]

emptylist = []

print("Milene" in data) # checks if Milene happens inside Data

print(users[0]) # will print the first item
print(users[-1]) # will print the last value

print(users.index('John'))

print(users[0:2]) # range of values but will not print number 2
print(users[-3:-1]) # its the same thing as saying [0:2] just like above
print(users[1:]) # also range of values but this way it will print number 1

print(len(data)) # counts how many items but the count does not start on zero

users.append('Elsa') # add items
print(users)

users += ['Jason'] # add items
print(users)

users.extend(['Robert', 'Jimmy']) # add items
print(users)

users.extend(data) # add items
print(users) 

users.insert(0, 'Bob') # add items in specific position
print(users)

users[2:2] = ['Eddie', 'Alex'] # add items in specific position
print(users)

users[1:3] = ['Rodrigo', 'JPG']
print(users)

users.remove('JPG')
print(users)

print(users.pop()) # retorna o valor retirado
print(users) # new updated list

del users[-1]
print(users)

# del data - returns a error
data.clear() # the right way of doing it
print(data)

users.sort() # ordena em ordem alfabética
print(users) 

nums = [4, 42, 11, 1991]
nums.reverse() # imprime de trás pra frente
print(nums)

nums.sort(reverse=True) # reorganiza os valores do maior para o menor e altera a lista original
print(nums)

print(sorted(nums, reverse=True)) # reorganiza os valores do maior para o menos sem alterar a lista original
print(nums)

# outra opção é fazer cópias para manipular sem alterar a lista original como nos 3 exemplos abaixo
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:] 

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# TUPLES is almost the same thing as List but the data and order will never change

mytuple = tuple(('Milene', 42, True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))




