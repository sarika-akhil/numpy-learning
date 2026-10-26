# IT IS FEATURE IN NUMPYS IT ALLOW TO PERFORM OPERATIONS AN ARRAYS OF DIFFERENT SHAPES WITHOUT MANUALLY RESIZING THEM 
#EXAMPLE:
import numpy as np
#arr1=np.array([[10,20,30],[20,40,50]])
#print(arr1+10) => [[20 30 40]
#                   [30 50 60]]
# IT ALSO CONATIONS 2 CONDITIONS IF THAT ARRAYS SATISFIY THAT CONDTIONS THEN WE CAN DO BROADCASTING
#1 IF THE SIZES OF THE BOTH COLUMNS ARE EQUAL
#2 IF ANY ONE OF THE ARRAY CONTAINS COLUMN SIZE IS 1 

# EXAMPLE FOR CONDITION 1
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]]) # here it is 2*3matrix that means 2 rows and 3 columns
arr2=np.array([1,2,3]) # here it is a 1*3 matrix that means 1 row 3 column
#NOTE: HERE COLUMNS SIZES ARE EQUAL SO BROADCASTING WORKS
#print(arr1+arr2) =>[[2 4 6]
#                    [5 7 9]] the output is in 2*2 matrix
# HERE WHAT IT DOES WAS IT CHANGES THE ARR2 FROM 1*3 MATRIX INTO 2*3 MATRIX AS SAME AS THE SIZE OF ARR1 
# IT TAKES THE ARR2 LIKE THIS[[1,2,3],[1,2,3]] IT TAKES THE SAME ELEMENTS IN THE 1ST ROW AS 2ND ROW 


#EXAMPLE FOR CONDITION 2:
import numpy as np
arr1=np.array([[10],
              [20],  # it the 3*1 matrix means 3rows and 1 column 
              [30]])
arr2=np.array([1,2,3]) # it is 1*3 matrix
#NOTE: HERE THE COLUMN THE SIZE OF ARR1 IS 1 SO WE CAN PERFOEM BROADCSATING
#print(arr1+arr2) =>[[11 12 13]
#                    [21 22 23] HERE THE OUTPUT IS IN THE FORM 3*3
#                    [31 32 33]]
# HERE WHAT BROADCASTING DONE WAS THE ARR1 IS IN THE SIZE OF 3*1 AND ARR2 WAS 1*3
# SO IT COVERTS BOTH ARRAYS INTO 3*3 MATRICES LIKE ARR1=[[10,10,10], AND ARR2=[[1,2,3], HERE OBSERVE IN ARR1 IT TAKES 1ST COLUMN ELEMENTS AS 2ND AND 3RD COLUMN AND ALSO IN ARR2 1ST ROW ELEMENTS AS 2 AND 3RD ROW
#                                                        [20,20,20],           [1,2,3],
#                                                        [30,30,30]]           [1,2,3]]       ]


#SEE THIS EXAMPLE :
import numpy as np
arr1=np.array([[1,2],
                [3,4], # here it is a 3*2 matrix
                [5,6]])
arr2=np.array([[1,2,3], # here it is a 1*3 matix
              [7,8,9]])
#NOTE: HERE IT DOESNT CONATION ANY 1 IN THE COLUMN SIZE AND ALSO THE COLUMN SIZES ARE NOT EQUAL SOO BROADCASTING DID NOT WORK HERE IF WE PRINT THIS WE WILL GOT AN ERROR
#print(arr1+arr2) => operands could not be broadcast together with shapes

