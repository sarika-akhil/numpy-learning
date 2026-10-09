# np.sum() => used to find the total sum
# np.mean() => used to find average
# np.min() => for finding minimum value
# np.max() => for finding large value
# np.std() => for standard deviation
# np.var() => for finding the varience
# np.median() => for finding the middle value
import numpy as np
list=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(list)
print(a)
#print(a.sum()) => [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
#                    45
#print(a.mean()) =  [[1 2 3]
#                   [4 5 6]
#                     [7 8 9]]
#                    5.0     =>sum of elements/noof elements= 45/9=5
#print(a.min()) => [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
#                    1

#print(a.max()) => [[1 2 3]
#                  [4 5 6]
#                  [7 8 9]]
#                   9

#  USING AXIS 
# IF AXIS =0 IT TAKE ROW REFRENECE AND GIVES THE COLUMN SUM
#EXAMPLE: TAKE THE SAME LIST AS INPUT AND PRINT THE SUM OF EACH column IN THAT LIST
#print(a.sum(axis=0)) ===>[[1 2 3]
#                          [4 5 6]
#                          [7 8 9]]
#                         [12 15 18]




# IF AIXS =1 IT TAKES COL REFRENCE AND GIVES THE row SUM
#EXAMPLE : SIMILARLY CALCULATE THE SUM OF EACH ROW
#print(a.sum(axis=1)) =>[[1 2 3]
#                        [4 5 6]
#                        [7 8 9]]
#                        [ 6 15 24]



#QUESTION : FIND THE SUM OF THE FIRST ROW THE LIST 
# WE ALREADY HAVE THE LIST [[1,2,3]
#                           [4,5,6,]     
#                           [7,8,9]] SO OUR ANSWER SHOULD BE 1+2+3=6
#print(a[0:1,:].sum()) =>[[1 2 3]
#                         [4 5 6]
#                         [7 8 9]]
#                         6