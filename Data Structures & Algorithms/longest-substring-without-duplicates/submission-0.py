class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_set = set()
        l = 0
        result = 0
        
        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l+= 1
            substring_set.add(s[r])
            result = max(result, r - l + 1)
        return result
            

        

  



       
        


        