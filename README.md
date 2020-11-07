# MetaheuriscApplications
This respository discusses about the application of metaheuristic search algorithm. Metaheuristic techniques are applied in solving the "Knapsack" problem

Knapsack Problem Defnition Given n diferent items, where each item i has an assigned value (vi) and weight (wi), select a combination of the items to maximize the total value without exceeding the weight limitations, W, of the knapsack.

Initial solution: The items are sorted in decreasing values in which the most valuable item is selected until the sum of weights is reached. 

Evaluation Function is given in the code. If the total Weight of selected items surpasses the max Weight, the total value is assigned with -1 

K-flip Neighborhood functions are implied. The basic code provides the 1-flip neighborhood, which is solved by taking out most valuable item and sorting from most to least value, until maximum weight is reached. The 2nd neighborhood was created for k-flip neighborhood. The solution for 2nd neighborhood will have 2nd most valuable item taken out and then items are collected from most to least value. 

#1 Hill Climb with Best Search

BFS is a search approach and not just a single algorithm, so there are many best-first (BFS) algorithms, such as greedy BFS, A* and B*. BFS algorithms are informed search algorithms, as opposed to uninformed search algorithms (such as breadth-first search, depth-first search, etc.), i.e. BFS algorithms make use of domain knowledge that can be encoded into a so-called heuristic function (that's why they are informed!).

#2 Hill Climb with First Improvements





