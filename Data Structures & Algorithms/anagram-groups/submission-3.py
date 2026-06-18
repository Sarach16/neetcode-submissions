from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return a list of lists
        #make a hashmap that maps letter freq to list of string
        mydict = defaultdict(list)
        freqlist = [0] * 26
        for s in strs:
            for char in s:
                freqlist[ord('a') - ord(char)] += 1
            mydict[tuple(freqlist)].append(s)
            freqlist = [0] * 26
        
        return list(mydict.values())






     
            
        
        


        