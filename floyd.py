import time

nums = [5, 2, 4, 5, 3, 1]

ptr1 = nums[0]
ptr2 = nums[0]

while ptr1 != ptr2:
    ptr1 = nums[ptr1]
    ptr2 = nums[nums[ptr2]]

ptr1 = nums[0]

while ptr1 != ptr2:
    ptr1 = nums[ptr1]
    ptr2 = nums[ptr2]

print(ptr1)
    