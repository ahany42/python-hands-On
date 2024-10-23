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
print(secondLargestNumber([1,2,8,7,6]))