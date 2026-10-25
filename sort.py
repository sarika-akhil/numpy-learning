#FOR SORTING NORMALLY WE USE SORT() METHOD 
#EXAMPLE:
#import numpy as np
#list=[10,2,13,4]
#a1=np.array(list)
#a2=a1.sort()
#print(a2) = it prints None 
#print(a1)  #=>[ 2  4 10 13] it prints the sorted array that means it changes the  original data 

# so for sorting without changing the original data we use np.sort() method
#EXAMPLE:
#import numpy as np
#arr1=np.array([10,2,13,4])
#arr1_ascend=np.sort(arr1) # it sorts the array in ascending order
#print(arr1_ascend) #  2  4 10 13] it prints this output and it doesnt disturb the original data 
#print(arr1) =>[10  2 13  4] the original data remains same

#FOR MULTIDIMENSIONAL ARRAYS 
#FOR THIS PURPOSE WE NEED TO USE AXIS=0 OR AXIS=1
#WKT AXIS=0 MEANS TAKE ROW PREFERENCE AND DOES THE COLUMN 
#    AXIS=1 MEANS TAKE COLUMN REFERENCE AND DOES THE ROW
#EXAMPLE:
#FOR COLUMN
#import numpy as np
#arr1=np.array([[4,2,9],[5,1,10]])
#arr1_ascend=np.sort(arr1,axis=0)
#print(arr1_ascend) =>[[ 4  1  9] => here it checks the elements in column wise like 4and5,2and1,9and10
#                      [ 5  2 10]]

#EXAMPLE FOR COLUMN:
import numpy as np
arr1=np.array([[4,2,9],[5,1,10]])
arr1_ascend=np.sort(arr1,axis=1)
print(arr1_ascend) #=>[[ 2  4  9]  here it checks row wise 4,2,9=2,4,9
#                     [ 1  5 10]]                          5,1,10=1,5,10

