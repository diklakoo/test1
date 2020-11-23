'''hobbies = []

# Add your code below!
for i in range(0,3):
  hobbies.append(input('Whats your hobby?'))
print (hobbies)

text = 'Whats your hobby?'
text.iS

print('Ex1:')

def asterisk(n):
 for i in range(n+1):
  print (('*')*i)
asterisk(5)

print('')
print('Ex2:')
print('')

def asterisk_t(n):
 for i in range(n):
  print (('*')*(i+4))
asterisk_t(4)

print('')
print('Ex3:')
print('')

def rhombus(n):
 half =int(n/2)
 for i in range(1,n):
  if i<n/2 :
   print(((' ')*(half-i))+(('*') * i))
  elif i == half:
    print((('*') * i))
  else:
   print(((' ')*(i-half)) +('*') * (n-i))

rhombus(10)


print ('  *' )
print (' ***' )
print ('*****' )
print (' ***' )
print ('  *' )

#  הדפסת מעוין----------------------------
num = 9

for i in range(1, num+1):
  i = i - (num//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (num - i*2) + " "*i)

--------------------------# לוח הכפל
for x in range(1,11):
  for y in range(1,11):
    print (f'{x*y:3d}',end=" ")
  print()'''

# יצירת רשימה רנדומלית
from statistics import mean

'''import random as rd
nums=[]
for i in range (15):
  nums.append(rd.randint(0,15) )
print(nums)
# מחיקת הערך 1 מהרשימה גם כשהוא מופיע יותר מפעם אחת
while 1 in nums:
  nums.remove(1)

print (nums)'''

# הפונקציה מקבלת רשימת מספרים, ומחזירה את המספר האמצעי אםיש מספר איברים אי זוגי, או ממוצע 2 המספרים האמצעיים אםמס' זוגי של איברים
'''import statistics

def median(list):
  list=sorted(list)
  long=len(list)
  if long % 2==0:
    mid_list= list[int(long/2)-1:int(long/2)+1]
    mid= statistics.mean(mid_list)
  else:
    mid=list[(long//2)]
  print (mid)
list1=[1,2,3,4,5,6,7,8,9,10,11,12]
median(list1)'''

'''
def match():
  import random
  random_n= random.randint(1,5)
  print(random_n)
  x= int(input('guess a number:'))
  while x!=random_n :
   if x>0 and x<random_n:
    print("it's too low")
    x = int(input('guess another number:'))
   else:
    print("it's too high")
    x = int(input('guess another number:'))
  print('You Win')
match()'''

'''def seven_boom():
 for x in range(1,51):
  if x%7==0:
    print('boom')
  else:
    print (x)

seven_boom()'''

'''
def next_number():
 for x in range(1,21):
  next= input('enter the next number:')
  if x % 7 == 0:
    if next =='boom':
      print (next)
    else:
      print ('you wrong')
      break
  else:
    if x == int(next):
      print(next)
    else:
      print('you wrong')
      break

next_number()
'''

'''def seven_boom_inteactive():
 turn=1
 for x in range(1,51):
  if turn %2==0:
   if x%7==0:
    print('boom')
   else:
    print (x)
  else:
    next = input('enter the next number:')
    if x % 7 == 0:
      if next == 'boom':
        print(next)
      else:
        print('you wrong')
        break
    else:
      if x == int(next):
        print(next)
      else:
        print('you wrong')
        break
  turn+=1
seven_boom_inteactive()'''
# תרגיל 1 מצגת 10 -----------------------------------------------------------------------
'''movies=['the notebook', 'maleficent', 'batnam V superman']
actors=['rachel macadams', 'angelina julie', 'gal gadot']
for i, j in zip(movies,actors):
  print (i + ' is played by ' + j)'''
# תרגיל 2+3 מצגת 10 -----------------------------------------------------------------------

'''movies=['the notebook', 'maleficent', 'batnam V superman']
actors=['rachel macadams', 'angelina julie', 'gal gadot']
union_dict= dict(zip(movies,actors))
[print (key + ' is played by ' + union_dict[key]) for key in union_dict]'''
# תרגיל 4 מצגת 10 -----------------------------------------------------------------------
'''list=list(range(1,10))
print([x*100 for x in list if x%2==0])

#אופציה ב' :

list1=list(range(1,10))
print (list(map(lambda x :x*100 ,filter(lambda x: x%2==0 ,list))))
# תרגיל 5 מצגת 10 -----------------------------------------------------------------------
print([x*100  if x%2==0 else x for x in range(10)])

#אופציה ב' :

print(list(map(lambda x: x*100  if x%2==0 else x, range(10))))
# תרגיל 6  מצגת 10 -----------------------------------------------------------------------
print([x if x%7!=0 else "boom" for x in range(1,100) ])

#אופציה ב' :

print (list(map(lambda x: "Boom" if  x%7==0 else x, range(1,100))))'''

# תרגיל 7  מצגת 10 -----------------------------------------------------------------------

'''sum= lambda x,y :x+y
print(sum(5,7))'''
# תרגיל 8  מצגת 10 -----------------------------------------------------------------------

'''listnew=[ (i,j) for i in range(1,7 ) for j in range(1,7)]
print(listnew)

# תרגיל 9  מצגת 10 -----------------------------------------------------------------------

joules=[5000,8000,10000,600,12000]
print([(j,j/4184) for j in joules])

# תרגיל 9  מצגת 10 -----------------------------------------------------------------------
languages=['HTML', 'JavaScript', 'Python', 'Ruby']
print(list(filter(lambda x: x=='Python',languages)))
# אופציה נוספת :
print([x for x in languages if x =='Python'])
# ****************************************************************************************

import random
temp=[random.randint(0,38) for n in range(30)]
print (temp)
print(['cold' if t<15 else 'nice' if t<25 else 'hot' for t in temp])'''

# שאלה  1 בתרגילים הקשים-שיכול אותיות  מצגת 10 -----------------------------------------------------------------------
'''
def isAnagram(s,t):
 t1=list(t)
 check="True"
 if len(s)==len(t):
   while check == 'True':
    for letter in s :
       if letter in t1:
           t1.remove(letter)
           check= 'True'
       else:
           check = 'False'
    return check
 else:
    return False

print(isAnagram('dikli','dikla') )


פתרון טוב יותר #

def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


s1 = "anagrams"
s2 = "anagramn"
check(s1, s2)

# שאלה  2 בתרגילים הקשים- תרגום מספר רומי-  מצגת 10 -----------------------------------------------------------------------#
def decimal_to_roman(decimal_number):
   roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
            100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
   amounts = sorted(roman.keys(), reverse=True)

   if 0 < decimal_number < 4000:
       roman_number = ''
       for amount in amounts:
           roman_number += roman[amount] * (decimal_number // amount) # חלוקה ב- // נותנת את המספר העגול ללא הנקודה העשרונית. כמו לעשות Int לכל הנוסחא
           decimal_number = decimal_number % amount
       return(roman_number)
   else:
       return None

print(decimal_to_roman(110))
print(decimal_to_roman(678))
print(decimal_to_roman(1234))
# שאלה  2 בתרגילים הקשים-פלוס 1 -  מצגת 10 -----------------------------------------------------------------------
def plus_one(digits):
 num= int( ''.join(map(str, digits)))+1
 digits_bigger = [int(x) for x in str(num)]
 
 
 print(digits_bigger)

digits= [9,9,9,9]
plus_one(digits)

'''


# -----------------------------------------------------------------------------------

class Tree:

    def __init__(self, value, left=None, right=None):

        self.left = left
        self.right = right
        self.value = value

    def PrintTree(self):
        print(self.value)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()


root = Tree(8)
root.left = Tree(3)
root.right = Tree(10)
root.PrintTree()

with open('20200130_070530.jpg', 'r') as f:
    pass


'''def power(x,y):
    assert (x>0),print( "x must be a pos num not {0}.".format(x))
    assert (y>0),print('y must be a pos num not {0}.'.format(y))
    return x*y
print (power(0,-6))'''





