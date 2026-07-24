class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # have a dict count of chars freq in t 
        # keep track of len 
        count = {}
        for char in t:
            count[char] = count.get(char, 0) + 1
        window = {}
        need = len(count)
        have = 0
        sub = ""
        subLen = float("inf")

        l = 0
        for r in range(len(s)):
            if s[r] in count:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == count[s[r]]:
                    have += 1
            while need == have:
                if (r - l + 1) < subLen:
                    sub = s[l:r+1]
                    subLen = r - l + 1
                window[s[l]] = window.get(s[l], 0) -1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
                
        return sub



                    
                

        
                

            

            

            


     





        