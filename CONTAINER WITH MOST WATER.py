class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        most_water_area=0
        while left<right:
            length=min(height[left],height[right])
            width=right-left
            most_water_area=max(most_water_area,length*width)

            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return most_water_area


# used 2 pointer approach from right and left 