a = "mahiya"


l =[10,20,30,40,50]
for i in l:
    print(i)

li= eval(input('enter your no:-'))
print(li)
total=1
for i in li:
    total = total*i
print(total)
#Range Datatype

for i in range(1,15):
    if i%2 !=1:
        print(i)

for i in range(1,100):
    if i%2  !=1:
        print(i)
a = 10
b = 20
if a<b:
    print(a ,'is greater than b')
a=50
b=100
if a<b:
    print('mai sonali hu')
s=('sonali')
a= ('Name','Age','Address')
c={}
print(c.fromkeys(a,s))
a = 10
b = 10
print(id(a))
print(id(b))
print(a is not b)

a=[10,20,30,40,52,60]
print(10 not in a)'''
a=10
b=40
x=50 if a>b else 60

print(x)


