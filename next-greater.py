# The nextGreaterElements method finds the next greater element for each element in a circular array.

# Use a stack to track elements for which the next greater value is not yet found.
# Traverse the array twice (simulate circular behavior):
# - For each element, remove smaller elements from the stack.
# - Assign the top of the stack as the next greater element if the stack is not empty.
# - Push the current element onto the stack.

# TC: O(n) - Each element is pushed and popped from the stack at most once.
# SC: O(n) - Space for the stack and result array.


from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums) * 2 - 1, -1, -1):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()
            res[i % len(nums)] = -1 if not stack else stack[-1]
            stack.append(nums[i % len(nums)])

        return res