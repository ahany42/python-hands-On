# hands on 1
# input  [[1,2,3],[4,5,6],[9,9,10],[7,8,9]]]
# return list with higher elements sum
# output [9,9,10]
def handsOn1(initialList):
  list = initialList
  li = [];
  maxSet = [];
  for x in list:
      li.append(sum(x))
  for x in list:
      if(sum(x) == max(li)):
        maxSet.append(x);
  print(maxSet)

#handsOn1([[1,2,3],[4,5,6],[9,9,10],[7,8,9]])

#hands on 2
# input 5 
# recursive f = f(n-1) + 100 , f(1) = 0
# output 501
def handsOn2(number):
  if(number == 0):
    return 1;
  else:
    return handsOn2(number - 1) + 100;
  
#print(handsOn2(5))

#hands on 3
#palindrome text
def is_palindrome(str):
    return str == str[::-1]

#hands on 4
def removeDuplicates (str) :
  return list(set(str))
#hands on 5 
def secondLargestNumber(list):
    li = removeDuplicates(list)
    li.sort()
    return li[2];
# print(secondLargestNumber([1,2,8,7,6]))

#hands on 6
class car:
  def __init__(self,model,year):
    self.model = model
    self.year  = year
    
  def printData(self):
    return self.model , self.year
  
c1 = car("Honda",2024)
# print(c1.printData())

 #hands on 7
def isEven (number):
  return (number % 2 == 0)

#hands on 8
def sumOfEven (list):
  sum = 0
  for x in list:
    if(isEven(x)):
      sum += x
    else:
      continue;
  return sum
#print(sumOfEven([1,2,3,4]))

#hands on 9
list1 = [1,2,3]
list2 = list1.copy()
list1.pop()
# print (list1)
# print (list2)

#hands on 10
def Fibonacci(number):
  if(number == 1):
    return 1
  elif(number == 0):
    return 0
  else:
    return Fibonacci(number-1) + Fibonacci(number-2)
  
# print(Fibonacci(10))

#hands on 11
#Input: [[1, 2], [3, 4], 5]
#Output: [1, 2, 3, 4, 5]
def FlattenList (li):
  newList = []
  for x in li:
    if isinstance(x, list): 
      newList.extend(x) 
    else:
      newList.append(x) 
  return newList

# print(FlattenList([[1, 2], [3, 4], 5]))

# hands on 12
class Human:
  def __init__(self,name,age,car):
    self.name = name
    self.age = age
    self.car = car
  def getCar(self):
    return self.car.model , self.car.year
  def getName(self):
    return self.name
  def getAge(self):
    return self.age
  
h1 = Human("Aly Hany",20,c1)
# print(h1.getCar())
# print(h1.getAge())
# print(h1.getName())

#hands on 13
def ReverseList(list):
  return list[::-1]
# print(ReverseList([1,2,3,4,5]))

#hands on 14
#tuples 
c1 = (1,2,3)
for x in c1:
  print(x)
for x in c1:
  print(x)
  
#hands on 15
# Check for Anagrams
# Question: Write a function that checks if two strings are anagrams 
# (contain the same characters in different orders).
# Example Input: "listen", "silent"
# Example Output: True
def anagrams(s1,s2):
  if(len(s1) != len(s2)):
    return False;
  else:
   return(sorted(s1) == sorted(s2))

print(anagrams("listen", "silent")) 

#hands on 16
#pop vs remove
#pop returns the element , remove is void
li = [1,2,3]
print(li.pop()) #=> 3
#print(li.remove()) error

#hands on 17
#inserting a value at index bigger than size + 1 will insert the value at the index of size
li.insert(100,3)
print(li)

#hands on 18
#find index of particular element
def FindIndexOf(number,li):
  print(li.index(number))
  
FindIndexOf(3,li)

#hands on 19
#inserting value in the same index of another value will shift the values 
li.insert(0,4)
print(li)

#hands on 20
#sorted vs sort
print(sorted(li))
#li is not saved sorted in memory
print(li)
#li is saved stored
li.sort()
print(li)

#hands on 21
#input integer
x = input("Enter a number\n")
x = int(x)
print(x*x)

#hands on 22
class Countdown:
  def __init__(self,number):
    self.number = number
  def Count(self):
    li = []
    for x in range (1,self.number+1):
        li.insert(0,x)
    return li
c2 = Countdown(5)
li = c2.Count()
for x in li:
    print(x)