def pickingNumbers(a):
    # Write your code here
    return max([((a.count(i)+ a.count(i+1))) for i in set(a)])
                
    

pickingNumbers([4,6,5,3,3,1])