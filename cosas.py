#import pandas as pd 

name = 'mao'
age = 12
like = 'cafe'

print(age)


#print('mi nombre es' + name + 'tengo' + str(age) 'me gusta el')


print(f'hello my name is {name} im {age} and i like so much {like}')

numbers =[1, 2, 3, 4, 5]
print(numbers)


fruits = ['mora', 'orange', 'apple', 'lemons', 'grape']
print(fruits)

print(fruits[0:3])
print(len(fruits))
fruits.append('mangos')

fruits.remove('lemons')

fruits.insert(3, 'cereza')




fruits.pop(4)

fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)
print(fruits)


