class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freq dict and sliding window
        # result windowLength - mostFreqCharCount + k
        count = {}
        l = 0
        result = 0
        maxfreq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxfreq = max(maxfreq, count[s[r]])
            while r - l + 1 - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1 )
        return result 
            

                

       

              
            
