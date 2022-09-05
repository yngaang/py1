a = [12,45,43,21,65,7,56,32,23,4,6,7,457,356,5,43,534,6] #задание 1. создать функцию для нахождения максимума 
print (a)
print (max(a))
def max1 (a):
    max=a[0]
    for elem in a:
        if max < elem:
            max = elem
    return max
print (max1(a))


s = ['asdsad','asdvc', 'gfgfdhgr', 'fsdfeyyy','gcvc', 'd','ggfd','gf'] #задание 2.1 с помощью метода addend создать функцию, которая принимает списко чисел и возращает список чётных чисел
print (s)
for elem in s:
    if len(elem)>4:
        print(elem)
a=[1, 2,6,3]
def chet(a):
    b = []
    for elem in a:
        if elem % 2 == 0:
            b.append(elem)
    return b
b=chet(a)
print(b)


def chet_nechet(a): #задание 2.2 с помощью метода addend создать функцию, которая принимает списко чисел и возращает два список чётных и нечётных чисел
    c = []
    n = []
    for elem in a:
        if elem % 2 == 0:
            c.append(elem)
        else:
            n.append(elem)
    return c,n
b=chet_nechet(a)
print(b)


def fact(a): #задание 3. создать функцию для нахождения факториала
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
print(fact(5))
print(fact(1))
print(fact(12))
