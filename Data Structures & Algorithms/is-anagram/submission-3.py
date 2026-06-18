class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_s =[0]*26
        list_t =[0]*26
        for char_s, char_t in zip(s,t):
            list_s[ord(char_s)-ord('a')]+= 1
            list_t[ord(char_t)-ord('a')] +=1 
        return list_s == list_t