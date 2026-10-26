#VECTORIZATION IS NOTHING BUT PERFORMING OPERATIONS ON WHOLE ARRAY RATHER THAN INDIVIDUAL ELEMENTS. IT IS MUCH FASTER THAN ITERATING THROUGH EACH ELEMENT OF THE ARRAY.
#LETS SEE AN EXAMPLE OF WITH AND WITHOUT VECTORIZATION
#WITHOUT VECTORIZATION  
#import numpy as np
#arr1=np.array([1,2,3,4,5])
#for i in range(len(arr1)):
#    arr1[i]=arr1[i]*2 
#print(arr1) =>[ 2  4  6  8 10]

#without vectorization
#import numpy as np
#arr1=np.array([1,2,3,4,5])
#print(arr1*2) =>[ 2  4  6  8 10] => this was the difference between with and without vectorization we didint want to iterate every single element in array 
                                    # we can directly perform that opertipn for the whole array 
#similarly we can do many operations like +,-,**,% anything like this 
#example
#import numpy as np
#arr1=np.array([4,5,6,7])
#print(arr1+2)=>[6 7 8 9] addition
#print(arr1-1) =>[3 4 5 6] substraction
#print(arr1**2) =>[16 25 36 49] power 2
#print(arr1%2) =>[0 1 0 1] modulo by 2
#print(arr1+arr1) =>[ 8 10 12 14] we can do arr1+arr1 or any thing like this 


#FOR TWO DIMENSIONAL ARRAYS
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([6,7,8,9])
#print(arr1+arr2) =>[ 7  9 11 13]
#print(arr1*arr2) =>[ 6 14 24 36]
#print(arr1-arr2) =>[-5 -5 -5 -5] like this you can do any opertions for this arrays not only 2D we can do for this process for multidimensional arrays