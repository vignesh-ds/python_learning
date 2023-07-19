# 1.Print
# print("hello world")

# 2.single line comment loop
# multiple line comment
# x ='vignesh'
# if x == 'sarah': # inline comment checking the match
#     print("match")
# else:
#     print("no match")
    
# 3. variable assign
# a,b,c = 15,20,25
# print(a)
# print(b) 
# print(c)   
# del c

# 4. datatypes
# a = 5
# b = 6.5
# c = 'vignesh'
# d = ['1','3','vignesh']
# e = {a:'37',b:'40'}
# f = {1,2,3}
# g = (1,2,3)

# print(type(a))
# print(type(b)) 
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

#5.function creation
# def printer(x):
#     return print("helloworld",x)

# printer("helloworld")

# 6.python input and output

# email = input("enter the mail_id :")
# print(email)

# num1 = input("enter n1:")
# num2 = input("enter n2:")

# print(num1+num2)

# input always take the value as string we need to change the data type explicitly

# num1 = input("enter n1:")
# num2 = input("enter n2:")

# print(int(num1)+int(num2))

#If,else,elif are all conditional flow commands and while ,for are loops

#bill amount > 100 discount 1 
#bill amount > 200 discount 2
#bill amount > 300 discount 3

# amount = 310
# discount1 = 10
# discount2 = 20
# discount3 = 30
# if (amount > 100 and amount < 200):
#     print("bill amount is between 100 to 200")
#     amount = amount - discount1
# elif (amount > 200 and amount < 300):
#     print("bill amount is between 200 to 300")
#     amount = amount - discount2
# elif (amount > 300 and amount < 400):
#     print("bill amount is between 300 to 400")
#     amount = amount - discount3    
# else:
#     print("bill amount less then 100 no discount")
    
# print('finalbill',amount)


# family = ['nirmala','lakshmi','sarah','vignesh']

# for i in family:
#     if i == 'nirmala':
#         print('mother')
#     elif i == 'vignesh':
#         print('husband')
#     elif i == 'lakshmi':
#         print('wife')
#     else:
#         print('daughter')
        
# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
# count = 0
# for count, value in enumerate(num_list):
#     count += 1
#     if value > 45:
#         print('Over 45',value)
#         break
#     elif value == 36:
#         print('Number found at position:',count)
#     else:
#         print('Under 45',value)
        
#print(count)
# tutorial on condition flow https://docs.python.org/3/tutorial/controlflow.html
# while and batch needs to be done
