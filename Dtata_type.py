#..1-BOLEAN DATA TYPE
# yes & no
# true & false

#..2-STRING DATA TYPE
# if you write a data in a quote('') means it is string.
# all the data u see in the keyboard and it is wirite in the ('') then it's string.
'''a = '100'
print(type(a))

b =('a','10','n','code')
print(type(a))

C = ('&','*','/','somkjgv','$#@$')
print(type(a))

#..-SLICING  ONCEPTS OF STRING
# -- FORMULA=[start:end+1+step]
# eg.
a = 'could you please help me once'
print(a[-5:])
name = 'sonali ravindra asane'
dob = '01-07-1994'
print(name[0:7]+dob[6:10])
print(b[7:16]

#--STRING FUNCTIONS--
#--1--UPPER
j = 'my name is sonali'
print(j.upper())
n = 'hellow word printed successfully'
print(n.upper())

b = 'ALL THE BEST!'
print(b.lower())

#--3--REPLACE
a = 'hello how are you'
print(a.replace('hello','shivansh'))

#--4--strip
#--strip method is used to delete the unvanted space from the string.
a='      man'
print(a)
print(a.strip())
b ='   pratap  '
print(b.strip())
c = 'prit    '
print(c.strip())

#--5--count
#--it counts no. alphabets,words,repeats how many times
b = 'my home my nane sona sona 1414255'
print(b.count('sona'))
h = 'shiv shiv shambho shmbho shiv shankara parvati shamnbohcbbasjsx'
print(h.count('o'))

print(len(s))

#--6-INDEX & FIND--
# find and index is a function shows the position of character in a string.
# only diffrancd in both find and index is that ,when we put word or alphabet that is not present in a string
# ,then index shows error and find function shows result -1.
a = 'i am lic agent'
print(a.find('o'))
print(a.index('o'))
b = 'yes am sonali all the amp'
print(b.index('amp'))

#- 7-ENDSWITH & STARTSWITH
#--endswith function shows string end with which word or alphabet if condition is satisfied then it gives result
s = 'i am sonali.'
print(s.endswith('.'))
print (s.startswith('m'))
#--8--swapcase
s = 'MY name IS sonali'
print(s.swapcase())

#--9-SPLIT
s ='abhiman abhilipsa abhiram ananya ayan'
print(s.split(' '))

#--10--JOIN
#--it is reverse process of split
l = ['abhiman ','abhiram','abhilipsa','abhimanyu']
A = '/'.join(l)
print(A)
print(type(A))
def test():
    a=10
    b=20
    print(a+b)
test()
a=10
def t1():

    print(a)

def t2():
    print(a)
t2()
t1()
#Local variables

def test():
    a=20

    print(a)
test()

def trust():
    print(a)
trust()

# Global keyword
a = 20
def shiv():
    a=108
    print('shiv',a)

def ravi():
    print('ravi',a)
shiv()
ravi()
a=30
def m():
    global a
    a=108
    print('m',a)
def m1():
    print('m1',a)
m()
m1()

b=20
def mod():
    global b
    b=100
    print(b)
def mod1():
    print(b)
mod()
mod1()'''
# list data type
# if we want to represent a group of entitites where insertion order is preserved and duploicates are allowed then we should go for list data type
# APPEND
# add only one data at one time
li=[1,2,3]
li.append(4)
print(li)
b=['sona','mona','priy',1,2]
b.append('mahi')
print(b)

#INSERT
# it also add onlyone dtata at a time ..with @ position u want
c= ['and','you','i',5]
c.insert(0,10)
print(c)

#CLEAR
#it clear data from list ..give empty list like truncate function
n =[12,1,5,3,52,2,00,2]
n. clear()
print(n)

#-3-COPY
#-it copy all items as it is --if some elements are present in b before it copying then that element will be erased.
m = [1,2,3,5,4]
b = [8,9]
b =m.copy()
print(b)

#-4 COUNT
# cont's how many times given element  are repeated
a = ['A','B','C','A','B','C','A','A','C']
print(a.count('A'))

#-5 EXTEND
# extend means simply add one list with another list as it is
li = ['a','mona','mahi',4]
za = [12,20,'oops']
li.extend(za)
print(li)

#-6-INDEX
# index function defines position of value even when another elements present in that but it gives first element
# position only
li =[40,50,2,0,11,40,40,'all','mahi','munna','munna','mahi']
print(li.index('munna'))

#-7 POP
#-from the given list last position data is deleted and show the list
li = [12,20,2,0,'m','e']
print(li.pop())
print(li)

#- 8 REMOVE
# it removes data that we want
li = [10,20,40,'E','EH','J']
li.remove('E')
print(li)

#-9 REVERSE
# it replicate list
li = [10,'i','ki','lisa']
li.reverse()
print(li)

#- 10-SORT
# it gives data in ascnending and descending format
#but cannat takes mix format data(number + char)
li = ['B','N','L','C','MAHI']

li.sort()
print(li)
m= ['B', 'N', 'L', 'C', 'MAHI']
m.sort(reverse=True)
print(m)

li = ['good morning','sonali','mahi','jolly']
li.append('preet')

print(li)

m = 'good morning sonali mahi jolly'
print(m.split(' '))





























