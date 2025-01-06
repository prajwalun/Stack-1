# The dailyTemperatures method calculates how many days it will take for a warmer temperature for each day.

# Use a stack to track temperatures and their indices:
# - For each temperature, pop from the stack while the current temperature is greater than the stack's top.
# - Calculate the difference in indices and update the result for the popped index.
# - Push the current temperature and its index onto the stack.

# TC: O(n) - Each temperature is pushed and popped from the stack once.
# SC: O(n) - Space for the stack and result array.


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res