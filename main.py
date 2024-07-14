# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.


st = 'as 345 rfhfrjfrhuruh68787ssd'
result=""
for i in st:
    if i.isdigit():
        result+=i


print(','.join(result))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st2='as 234 jdfbjhefb25 4859'
result2=[]
current_item=''
for i in st2:
    if i.isdigit():
        current_item+=i
    elif current_item:
        result2.append(current_item)
        current_item=''
if current_item:
    result2.append(current_item)
    print(','.join(result2))


# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

Comp_list=[x.upper() for x in greeting]
print(Comp_list)

# з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

range_smart= [i**2 for i in range(50) if i/2!=0]
print(range_smart)

# function
#
# - створити функцію яка виводить ліст
str3= 'hi my name is bob im 26'

def appendlist(str3):
    listtizer = []
    for index in str3:
         listtizer.append(index)


    return print(listtizer)


appendlist(str3)
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def maxidentifier(x,y,z):
    return print(max(x,y,z))
maxidentifier(2,5,10)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_returne_maxprintrer(*args):
    print(max(args))
    res123=min(args)
    return res123




min_returne_maxprintrer(1,34439439,2,3,45,5,67,76,878,78,7878)
# print(res123)
# - створити функцію яка повертає найбільше число з ліста
listmax=[1,5,2,150,2,10550,0,1]
def max_listi(list):
    maxres=max(list)
    return maxres

maxres=max_listi(listmax)
print(maxres)

# - створити функцію яка повертає найменьше число з ліста
def minfromlist(list):
    return min(list)

minres=minfromlist(listmax)
print(minres)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def lisitemsum(list):
    return sum(list)

suma=lisitemsum(listmax)
print(suma)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def listav(list):
    average=sum(list)/len(list)
    return average
averagefromlist=listav(listmax)
print(averagefromlist)


# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
list23 = [22, 3,5,2,8,2,23, 8,23,5,100]
list24 = [22, 3,5,2,8,2,23, 8,23,5,100,0]
def min_lis(lis):
    print(min(lis))
min_lis(list23)
min_lis(list24)
print(list(set(list23)))
def every4replace(lst,replacement):
    for i in range(3,len(lst),4):
         lst[i]=replacement

e4=every4replace(list23,'x')
print('modified list',list23)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def draw_empty_square(side_length):
    for i in range(side_length):
        if i == 0 or i == side_length - 1:

            print("* " * side_length)
        else:

            print("*" + " " * (side_length * 2 - 3) + "*")
draw_empty_square(5)

# 3) вывести табличку множення за допомогою цикла while
def multi_table():
    size=9
    i=1
    while i<=size:
        j=1
        while j<=size:
            res=i*j
            print(''if res//10 else ' ', end=' ')
            print(res, end='')
            j+=1
        print()
        i+=1

multi_table()

# 4) переробити це завдання під меню
while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на X')
    print('4)  вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('0) вихід')

    choice=input('enter your choice:')

    if choice=='1':
        min_lis(list24)
    elif choice == '2':
        print(list(set(list23)))

    elif choice=='3':
        every4replace(list23,'Y')
        print('modified list', list23)

    elif choice == '4':
        draw_empty_square(10)

    elif choice=='5':
        multi_table()

    elif choice=='0':
        break





















