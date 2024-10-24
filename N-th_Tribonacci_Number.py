# Leet Code 75:  1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        
        for i in range(3, n + 1):
            next_trib = a + b + c
            a = b
            b = c
            c = next_trib
            print(f'i is {i}, after exchange, a is {a}, b is {b}, c is {c}, next_trib is {next_trib}')
        
        return c
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.tribonacci(12)