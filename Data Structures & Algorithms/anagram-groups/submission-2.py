from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #list of lists 
        #create a dictionary of frequencies 

        dicts = collections.defaultdict(list)

        #initialise a list with the size of the alphabets
        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char)-ord('a')] +=1 #[1,0,1,...,1,0..]
            
            dicts[tuple(count)].append(str)
        
 
        
        return [strs for strs in dicts.values()]
            
        
        


        