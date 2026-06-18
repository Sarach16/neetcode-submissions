class Solution:
    def isValid(self, s: str) -> bool:
        #s is made of a combination of () {} []
        # order matters 
        #edge case ([()][()])
        #create a dict with 'opening' as key and 'closing' as value
        #first and last should close each other
        dicts = {'(':')','[':']','{':'}'}
        # s[len(s)-1]== dicts[s[0]] #this checks for the 1st and 2nd
        opening = []
        for char in s:
            if char in dicts.keys():
                opening.append(char)
            elif opening and char == dicts[opening[-1]]:
                opening.pop()
            else:
                return False
        return len(opening) == 0

