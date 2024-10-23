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