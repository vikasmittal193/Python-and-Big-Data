#!/usr/bin/env python
# coding: utf-8

# merge sort
def merge(numbers,i,j,k):
    mergedsize = k - i + 1
    mergednumbers = [None] * mergedsize
    leftpos = i
    rightpos = j+1
    mergepos = 0
    
    #adding smallest element from left or right to merged numbers
    while((leftpos <=j) and (rightpos <=k)):
        if(numbers[leftpos] < numbers[rightpos]):
            mergednumbers[mergepos] = numbers[leftpos]
            leftpos+=1
        else:
            mergednumbers[mergepos] = numbers[rightpos]
            rightpos+=1
        mergepos+=1
    
    # if left partition is not empty, add remaining to mergednumbers list
    while(leftpos <=j):
        mergednumbers[mergepos] = numbers[leftpos]
        leftpos+=1
        mergepos+=1
    
    #similarly, if right partition is not empty, add remaining to mergednumbers list
    while(rightpos <=k):
        mergednumbers[mergepos] = numbers[rightpos]
        rightpos+=1
        mergepos+=1
        
    #copy mergednumbers to numebrs
    for mergepos in range(0,mergedsize):
        numbers[i+mergepos] = mergednumbers[mergepos]
        
        
def mergesort(numbners, i , k):
    j = 0
    
    if(i < k):
        j = int((k+i)/2)
        #recusrively sort left and right partitions
        mergesort(numbers,i,j)
        mergesort(numbers,j+1,k)
        
        #merge left and right partitions in sorted order
        merge(numbers,i,j,k)
        

if __name__ == "__main__":
    numbers = [10, 2, 78, 4, 45, 32, 7, 11]
    print(numbers)
    i=0
    k = len(numbers) -1
    mergesort(numbers,i,k)
    
    print(numbers)

'''
The merge sort algorithm's runtime is O(N log N). Merge sort divides the input in half until a list of 1 element is reached, 
which requires log N partitioning levels. At each level, the algorithm does about N comparisons 
selecting and copying elements from the left and right partitions, yielding N * log N comparisons.

Merge sort requires O(N) additional memory elements for the temporary array of merged elements.

For N elements, the number of levels is log N
'''


