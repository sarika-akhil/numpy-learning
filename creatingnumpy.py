#import numpy as np
#list=[1,2,3,4,5]
#arr1=np.array(list) # =>it converts normal list onto numpy array
#print(arr1) => [1 2 3 4 5]  => these elements are separated by spaces
#print(type(arr1))  => class np.ndarray   here nd means n dimensional array 


# CONVERTING TWO LISTS INTO 2D ARRAY
#import numpy as np
#list=[[1,2,3,4,5],[6,7,8,9,10]]
#arr=np.array(list)
#print(arr) => [[1 2 3 4 5]
 #              [6,7,8,9,10]]   =>2D ARRAY
  



# np.one((size)) METHOD IN NUMPY   => this method is used to create arrays with some specified row size and column size but this method prints only 1s as shown in the output 

#import numpy as np
#one=np.ones((2,3))
#print(one) ==>[[1. 1. 1.]
#              [1. 1. 1.]] => we gave (2,3) that means noof rows =2 and noof columns =3 
    
 # SIMILARLY np.zeros((size))   ==> it was also like that 1s but it prints all zeros




# NEXT METHOD IS np.arrange 
# `THIS METHOD IS USED TO CREATE A NUMPY ARRAY CONTAINING SEQUENCE OF NUMBERS 
 # EXAMPLES :
# WE CAN DO THIS IN 3 TYPES 
#1.np.arange(range)
#import numpy as np
#a=np.arange(4)
#print(a)  =>[0 1 2 3] => starts with 0 so its stops before your range number


#2. np.arange(start,stop)
#import numpy as np
#a=np.arange(2,7)
#print(a) =>[2 3 4 5 6]
  
#3.np.arange(start,stop,step)
#import numpy as np 
#a=np.arange(2,10,2)
#print(a) =>[2 4 6 8]




# next method as np.reshape() ===> THIS METHOD IS UDES TO CHANGE THE SHAPE OF THE NUMPY ARRAY WITHOUT CHANGING ITS ELEMENTS
#example:
#import numpy as np
#a=np.arange(1,7)
#print(a) => [1 2 3 4 5 6]
#print(a.reshape(2,3)) =>[[1 2 3]
#                        [4 5 6]] => HERE WE CHANGED THAT 1D NUMPY ARRAY INTO 2D ARRAY BY GIVING (2,3) BEACUSE IT WAS 6 ELEMENTS WE CAN MAKE 3 ROWS AND 3 COLUMNS AND ALSO 2 ROWS AND 3 COLUMNS IF WE TRY TO MAKE ANYTHING INSRAED OF THIS WE WILL GOT AN ERROR
