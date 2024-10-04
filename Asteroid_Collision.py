# Leetcode 75: 735. Asteroid Collision
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        j = 0  # This is a pointer to track the current index where we will place the asteroid in the modified list.
        n = len(asteroids)  # n is the total number of asteroids.
        
        for i in range(n):  # Loop through each asteroid one by one.
            asteroid = asteroids[i]  # Current asteroid being processed.
            
            # This loop handles the collision between a right-moving asteroid (positive) and a left-moving asteroid (negative).
            while j > 0 and asteroids[j - 1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
                j -= 1  # The smaller right-moving asteroid (positive) at asteroids[j-1] gets destroyed, move the pointer `j` back.
                print(f'j is {j}')
            
            # This `if` block handles cases where the current asteroid should be added to the result.
            # It happens in the following conditions:
            # 1. No asteroid to the left (j == 0), or
            # 2. Current asteroid is moving to the right (asteroid > 0), or
            # 3. The last asteroid in the result is moving to the left (asteroids[j-1] < 0), so no collision happens.
            if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
                asteroids[j] = asteroid  # Place the current asteroid in the valid position.
                j += 1  # Move `j` forward to indicate the valid portion of the list.
                print(f'asteroids:{asteroids}')
            # This `elif` handles the case where the two asteroids have the same size and collide.
            # When the absolute value of the current asteroid equals the asteroid in the previous position (ast[j-1]),
            # both asteroids get destroyed, so we move the pointer `j` back by 1.
            elif asteroids[j - 1] == abs(asteroid):
                j -= 1  # Both asteroids explode, so we just move `j` back by 1.
                print(f'elif: j :{j}')
        
        # Return the final state of asteroids after collisions. `asteroids[:j]` represents the valid portion of the list.
        return asteroids[:j]
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.asteroidCollision([10,2,-5,-3,8,-10,9,-2])
    print(f'the result is {result}')