# Leet Code 75： 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # left =1
        # right = n

        # while left <= right:
        #     # use //
        #     middle = (right + left)//2
        #     result = guess(middle)
        #     if result == 0:
        #         return middle
        #     elif result == -1:
        #         right = middle -1
        #     else:
        #         left = middle+1
        # return -1

        lowerBound, upperBound = 1, n
        # Binary division faster than (lowerBound + upperBound) //2
        myGuess = (lowerBound+upperBound) >> 1
        # walrus operator ':=' - assigns value of the function to the variable 'res'
        # and then compare res with 0
        while (res := guess(myGuess)) != 0:
            if res == 1:
                lowerBound = myGuess+1
            else:
                upperBound = myGuess-1
            myGuess = (lowerBound+upperBound) >> 1

        return myGuess

