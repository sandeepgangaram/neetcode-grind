class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        i=0
        while nums[i] <= 0 and i < len(nums)-2:
            if i>0 and nums[i] == nums[i-1]: #already seen
                i+=1
                continue

            possible_nums = self.getThreeNums(nums[i+1:],-nums[i])
            out +=possible_nums
            i+=1
        return out
                
    def getThreeNums(self, nums, target):
        out = []
        i,j = 0,len(nums)-1

        while i<j:
            if i>0 and nums[i] == nums[i-1]:
                i+=1
                continue
            curr_sum = nums[i] + nums[j]
            if curr_sum == target:
                out.append([nums[i], nums[j], -target])
                i+=1
                j-=1
            elif curr_sum > target:
                j-=1
            else:
                i+=1

        return out

        

        