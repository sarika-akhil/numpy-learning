#filter means slecting the elements that satifies a condition
#eg:
#import numpy as np
#a=np.array([10,20,30,40,50])
#condition= a>30
#print(a[a>30]) =>[40 50] here we gave condition as greater than 30 so it selected the values that are greater than 30
#print(a>30)  =>[False False False  True  True] here it gave the boolean values for the condition we gave

   
#WHERE FUNCTION MEANS SELECTING THE ELEMENTS THAT SATISFIES A CONDITION AND REPLACING THEM WITH OTHER VALUES

#FOR PRINTING THE VALUES 
#import numpy as np
#a=np.array([10,20,30,40,50])    
#print(a[np.where(a>18)]) =>[20 30 40 50]  #here we gave condition as greater than 18 so it selected the values that are greater than 18 and replaced them with major and the rest with minor
 

#FOR PRINTING THE INDICES
#import numpy as np
#a=np.array([10,20,30,40,50])
#print(np.where(a>18))  =>(array([1, 2, 3, 4]),)  #here we gave condition as greater than 18 so it selected the indices of the values that are greater than 18



#import numpy as np
#a=np.array([10,20,30,40,50])    
#res=np.where(a>18,'major','minor')  #here we gave condition as greater than 18 so it selected the values that are greater than 18 and replaced them with major and the rest with minor
#print(res)  =>['minor' 'major' 'major' 'major' 'major]



 #             Filter vs np.where()
#Filtering                                                       	                  np.where()
#Used to select elements that satisfy a condition.                   	Used to find positions/indices where a condition is true, or choose values based on a condition.
#Usually done using Boolean indexing.	It is a NumPy function.
#Returns the actual elements/values that satisfy the condition.	      In its one-condition form, returns the indices where the condition is true.
#Syntax: array[condition]	                                                 Syntax: np.where(condition)
#Mainly used for selecting/filtering data.	                          Used for finding positions or making conditional replacements/selections.


#One-line notes
#Filtering:  
#Filtering is the process of selecting elements from a NumPy array that satisfy a given condition.

#np.where():  
#np.where() is a NumPy function used to find the indices where a condition is true or select values based on a condition.


#ages who are eligible to vote and their ages must be less than 60
