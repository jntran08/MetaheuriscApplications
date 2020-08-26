#basic hill climbing search provided as base code for the DSA/ISE 5113 course

#NOTE: YOU MAY CHANGE ALMOST ANYTHING YOU LIKE IN THIS CODE.  
#However, I would like all students to have the same problem instance, therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 150)
#   random problem instance
#   weight limit of the knapsack

#------------------------------------------------------------------------------
#Student name: Ngoc Tran
#Date: 04/01/2020


#need some python libraries
import copy
from random import Random   #need this for the random number generation -- do not change
import numpy as np
import numpy as np


#to setup a random number generator, we will specify a "seed" value
#need this for the random number generation -- do not change
seed = 5113
myPRNG = Random(seed)

#to get a random number between 0 and 1, use this:             myPRNG.random()
#to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
#to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

#number of elements in a solution
n = 150

#create an "instance" for the knapsack problem
value = []
for i in range(0,n):
    value.append(round(myPRNG.triangular(5,1000,200),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(10,200,60),1))
    
#define max weight for the knapsack
maxWeight = 1500

#change anything you like below this line ------------------------------------

#monitor the number of solutions evaluated
solutionsChecked = 0

#function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(value)
    c=np.array(weights)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
    
    if totalWeight > maxWeight:
        #print ("Oh no! The solution is infeasible!  What to do?  What to do?") you will probably want to change this...
        totalValue = -1
        
    return [totalValue, totalWeight]   #returns a list of both total value and total weight
          
       
#here is a simple function to create a neighborhood
#1-flip neighborhood of solution x         
def neighborhood(x):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
    
    k_nbrhood= []
    
#k-flip neigborhood of solution x

    k = 2
    for i in range(0,n-k):
        k_nbrhood.append(x[:])
        for j in range(0,k):
            if k_nbrhood[i][i+j] == 1:
                k_nbrhood[i][i+j]=0
            else:
                k_nbrhood[i][i+j]=1
            
    return [nbrhood, k_nbrhood]

#create the initial solution

def initial_solution(value, weights):
    x = [0]*n   #i recommend creating the solution as a list
    sumWeights =0
    
    #rank the value array in descending order
    b= np.array(value)
    temp=b.argsort()
    rankVal= np.empty_like(temp)
    rankVal= np.arange(len(b))
    
    #assign item until the sum of weights exceeds maximum weights
    for i in range(n,0,-1):
        for j in range(n,0):
            if sumWeights < maxWeight:
                if rankVal[j] == i:
                    sumWeights = sumWeights+ weights[j]
                    if sumWeights < maxWeight:
                        x[j] =1
    return x

#varaible to record the number of solutions evaluated
solutionsChecked = 0

x_curr = initial_solution(value, weights)  #x_curr will hold the current solution 
x_best = x_curr[:]           #x_best will hold the best solution 
f_curr = evaluate(x_curr)   #f_curr will hold the evaluation of the current soluton 
f_best = f_curr[:]


#begin local search overall logic ----------------
done = 0
    
while done == 0:
            
    #create a list of all neighbors in the neighborhood of x_curr
    Neighborhood= neighborhood(x_curr)[1]
    
    for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        if evaluate(s)[0] > f_best[0]:   
            x_best = s[:]                 #find the best member and keep track of that solution
            f_best = evaluate(s)[:]       #and store its evaluation  
    
    if f_best == f_curr:               #if there were no improving solutions in the neighborhood
        done = 1
    else:
        
        x_curr = x_best[:]         #else: move to the neighbor solution and continue
        f_curr = f_best[:]         #evalute the current solution
        
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best value found so far: ", f_best)        
    
print ("\nFinal number of solutions checked: ", solutionsChecked)
print ("Best value found: ", f_best[0])
print ("Weight is: ", f_best[1])
print ("Total number of items selected: ", np.sum(x_best))
print ("Best solution: ", x_best)
