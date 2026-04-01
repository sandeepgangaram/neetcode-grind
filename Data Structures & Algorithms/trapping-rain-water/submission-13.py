class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <=2:
            return 0
        pre_max=[0]
        suf_max=[0]
        
        curr_pre_max = 0
        curr_suf_max = 0
        for i in range(1,len(height)):
            curr_pre_max = max(height[i-1],curr_pre_max)
            pre_max.append(curr_pre_max)
        for i in range(len(height)-2,-1,-1):
            curr_suf_max = max(height[i+1],curr_suf_max)
            suf_max = [curr_suf_max] + suf_max
        i=1
        total_area = 0
        print(pre_max,suf_max)
        while i+1 < len(height):
            l = height[i-1]
            m = height[i]
            r = height[i+1]

            if m<pre_max[i] or m<suf_max[i]:
                area = min(pre_max[i],suf_max[i]) - m
                total_area += area if area >0 else 0
                print(i,area,total_area)
            i+=1
        return total_area




        
            



     






        