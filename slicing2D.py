#import numpy as np
#list=[[1,2,3],[4,5,6],[7,8,9]]  #2D array
#a1=np.array(list)
#print(a1[0:1,]) =>[[1 2 3]] HERE WE GAVE CONDITIONS ONE FOR ROW ANOTHER FOR COLUMN
#IN FIRST CONDITION WE GAVE 0:1 SO IT SELECTED 0TH ROW AND IN SECOND CONDITION WE DIDN'T GIVE ANYTHING SO IT SELECTED ALL THE 
 
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[ :  ,2:])