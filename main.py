#------------------------------------------------------------------------#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#------------------------------------------------------------------------#

def main(max=9999, min=1000):
    print("the largest Palendrome is ", attempt2(max, min))

#------------------------------------------------------------------------#
# Function: attempt1
# Input: max - the maximum number to check defaults to 999
#        min - the minimum number to check defaults to 100
# Output: int - the largest palindrome found
# Description : A quick to develop soultion that checks every number. Many inprovemnts could be made
#               such as starting from the largest number and working down. This would be more efficient
#               becasue an early escape mechinisim could be used to stop checking numbers once a palindrome 
#               is found reducing the time complexity of the method from its current O(n^2). 
#------------------------------------------------------------------------#

def attempt1(max=999, min=100):
    max_palindrome = 0
    for i in range(min, max + 1):
        for j in range(min, max + 1):
            if(is_palindrome(i*j) and i*j > max_palindrome):
                print(i*j)
                max_palindrome = i*j
       
#------------------------------------------------------------------------#
# Function: attempt2
# Input: max - the maximum number to check defaults to 999
#        min - the minimum number to check defaults to 100
# Output: int - the largest palindrome found
# Description : An interation of the first attempt that uses numpy to vectorize the multiplication of the numbers.
#               Additionally it uses an escape clause to stop checking numbers once a palindrome is found. It checks 
#               the remaining diagonial of the matrix to see if a larger palindrome is found.Further improvements could
#               be made by only checking half of the digonal. Due to the multiplicative properity 99 x 11 = 11 x 99. 
#               The program still checks both of these numbers.
#------------------------------------------------------------------------#
import numpy as np         
def attempt2(max=1, min=10):
    #Create a matrix of all the products
    #Idea is to make the muliplication vectorizable using numpy
    vectorNum = np.arange(min, max + 1)
    productTable = np.outer(vectorNum, vectorNum)
    
    #Sample data from the product table
    #---------------------------------------#
    # 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 
    # 2 | 4 | 6 | 8 | 10| 12| 14| 16| 18| 20
    # 3 | 6 | 9 | 12| 15| 18| 21| 24| 27| 30
    # ... 
    #---------------------------------------#
    
    largestPalindrome = -1
    count = 0
    
    #Check the diagonals of the matrix, if a palindrome is found then check the remaining diagonal
    while(largestPalindrome == -1):
        if(count >= productTable.shape[0]):
            print("No palindrome found")
            return None
        
        #Init the staring position
        curentPostion = [len(productTable) - 1, len(productTable) - 1 - count]
        
        #Boundry conditions for moving in a diagonal
        while(curentPostion[0] >= 0 and curentPostion[1] < productTable.shape[1]):
            
            #print(curentPostion, productTable[curentPostion[0], curentPostion[1]])
            
            if(is_palindrome(productTable[curentPostion[0], curentPostion[1]]) 
               and productTable[curentPostion[0], curentPostion[1]] > largestPalindrome):
                largestPalindrome = productTable[curentPostion[0], curentPostion[1]]
                print("Current largest Palindrome is ", largestPalindrome)
                
            #Move in a diagonal
            curentPostion[0] -= 1
            curentPostion[1] += 1
        
        count += 1
        
    return largestPalindrome

#------------------------------------------------------------------------#
# Function: attempt3
# Input: max - the maximum number to check defaults to 999
#        min - the minimum number to check defaults to 100
# Output: int - the largest palindrome found
# Description : While this algorithm is not as efficient as the second attempt, I wanted to try to make it
#               into a single line. This is a good example of how python can be used to make code more readable.
#               However, it is not as efficient as the second attempt and has all of the same issues that the
#               first attempt has.
#------------------------------------------------------------------------#
def attempt3(max=999, min=100):
    #np.max is used to find the largest palindrome, max is used as a variable so complier was getting confused
    return np.max([i*j for i in range(min, max + 1) for j in range(min, max + 1) if is_palindrome(i*j)])

#attmpet 4
def attempt4(maxNumber = 999, minNumber = 100):
    largestPalindrome = -1
    count = 0
    difference = maxNumber-minNumber
    
    #Check the diagonals of the matrix, if a palindrome is found then check the remaining diagonal
    while(largestPalindrome == -1):
        if(count >= difference):
            print("No palindrome found")
            return None
        
        #Init the staring position
        curentPostion = [maxNumber, maxNumber - count]
        print(f"the current starting position is {curentPostion}")
        
        #Boundry conditions for moving in a diagonal
        while(curentPostion[0] >= 0 and curentPostion[1] <= maxNumber):
            
            #print(curentPostion, productTable[curentPostion[0], curentPostion[1]])
            product = (curentPostion[0]) * (curentPostion[1])
            
            if(is_palindrome(product) 
               and product > largestPalindrome):
                largestPalindrome = product
                print("Current largest Palindrome is ", largestPalindrome)
                
            #Move in a diagonal
            curentPostion[0] -= 1
            curentPostion[1] += 1
        
        count += 1
        
    return largestPalindrome
    
#Simple function to check if a number is a palindrome              
def is_palindrome(num):
    return str(num) == str(num)[::-1]


if(__name__ == '__main__'):
    #print(attempt3(999, 100))
    print(attempt4(10**14-1, 10**13))
