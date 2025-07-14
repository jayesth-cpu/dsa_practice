"""
01. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

✅ Constraints:
- Exactly one solution exists.
- You cannot use the same element twice.
- Return the indices in any order.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Approach:

1️⃣ Brute Force:
- Use two nested loops to check each pair of indices.
- If nums[i] + nums[j] == target, return [i, j].
- Time: O(n^2), Space: O(1)

2️⃣ Optimized using HashMap:
- Use a dictionary to store {number: index}.
- For each element, compute complement = target - number.
- If complement is found in the dictionary, return [dict[complement], current index].
- Time: O(n), Space: O(n)

# Implement your function below:
def two_sum(nums, target):
    pass

if __name__ == "__main__":
    # Write your test cases here to run and debug
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Expected: [0, 1]
"""


def two_sum(nums, target):
    dict = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in dict:
            return [dict[complement], index]
        dict[number] = index
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
