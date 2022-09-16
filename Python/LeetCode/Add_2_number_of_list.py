# target=int(input("Enter a number grater than 9 : "))
# li=[1,2,3,4,5,6,7,8,9,0]
# for i in range(int(len(li))): 
#     for j in range(i+1,int(len(li))):
#         if int(li[i])+int(li[j])==target:
#             print(f"[{i},{j}]")

# class Solution:
#     def twoSum(self, nums, target):
#         length=len(nums)
#         for i in range(length):
#             for j in range(i + 1, length):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
# target=int(input("Enter a number:"))
# li=[1,2,3,4,5,6,7,8,9,0]
# obj=Solution()
# print(obj.twoSum(li,target))