# Leetcode 75: 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''
        
        for char in s:
            print(f'The current char is {char}')
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Build the current number if it has more than one digit
                print(f'The current_num is {current_num}')
            elif char == '[':
                # Push the current string and number to stack, then reset them
                stack.append((current_str, current_num))
                current_str = ''
                current_num = 0
                print(f'After the [ , the stack is {stack}')
            elif char == ']':
                # Pop from stack and decode the string
                last_str, num = stack.pop()
                current_str = last_str + num * current_str
                print(f'After the ] , the stack is {stack}')
                print(f'After the ] , the last_str is {last_str}, the num is {num}')
                print(f'After the ] , the current_str is {current_str}')
            else:
                current_str += char  # Add characters to the current string
        
        return current_str
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.decodeString("3[a2[c]]")
    print(f'the result is {result}')