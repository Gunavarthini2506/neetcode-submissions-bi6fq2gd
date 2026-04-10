class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Total=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product*=nums[j]
            Total.append(product)
        return Total
            