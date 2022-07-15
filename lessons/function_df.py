"""An example function definition."""

# Write a Python program to calculate the sum of a list of numbers. Go to the editor
def list_sum(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else: 
        return nums[0] + list_sum(nums[1:])


listy: list[int] = [2, 4, 5, 6, 7]
print(list_sum(listy))

# Write a Python program to converting an Integer to a string in any base.

def factorial(factor: int) -> int:
    """Determine the factorial give a number."""
    if factor == 0:
        return 1
    if factor == 1:
        return 1
    elif factor != 1:
        return factor * factorial(factor - 1)

