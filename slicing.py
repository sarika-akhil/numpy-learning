#SLICING  MEANS SELECTING A PORTION OF AN ARRAY instead of taking whole array
# syntax= array[start:stop:step]
# starts =where to start 
# stop =where to stop(not included)
# steps =how many posistions to jump


#eg:
#import numpy as np
#a=np.array([10,20,30,40,70])
#print(a[1:3]) =>[20 30] here 4 th index was 70 
#NOTE: HERE WE GAVE START AND STOP VALUES SO IT STARTS FROM 1ST INDEX AND STOPS BEFORE 3RD INDEX

#EG 2:
#import numpy as np
#a=np.arange(1,9)
#print(a[2:6]) => [3 4 5 6] similarly it was also like ths


#eg 3:
#import numpy as np
#a=np.arange(1,10)
#print(a[1:12:2]) =>[2 4 6 8] here we gave 1 asstarting and 12 as ending and we gave step as 2 so it jumps 2 2 steps like index 1 value 2 next 2 steps increase soo 4 next 2 steps 6 next 8 and it stops beacuse we gave 10 as stop


# we can do slicing in negatuve indexes also
#eg:
#import numpy as np
#a=np.array([1,2,3,4,5,6,7,8,9])
#print(a[-4:-1]) =>[6 7 8]

#using step in negative index
#import numpy as np
#a=np.array([1,2,3,4,5,6,7,8])
#print(a[-8:-1:2]) =>[1 3 5 7]