class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s ={}
        dict_t={}
         
        if len(s)!= len(t):
            return False

        
        

        for char in s: 
            if char not in dict_s:
                dict_s[char]=1
            else:
                dict_s[char]+=1
        for char in t:
            if char not in dict_t:
                dict_t[char]=1
            else:
                dict_t[char]+=1
        return dict_s == dict_t
        
        

         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
            # #check if s and t have same length
            # #if not return false
            # if len(s) != len(t):
            #     return False
            
            # #create empty dictonary
            # #Loop through char in s 
            # #if char is not in dict add char 
            # #else increment value of char
            # dict_s = {}
            # dict_t ={}
            # for char in s:
            #     if char not in dict_s:
            #         dict_s[char]=1
            #     else:
            #         dict_s[char]+= 1
            # #do the same to t
            # for char in t:
            #     if char not in dict_t:
            #         dict_t[char]=1
            #     else:
            #         dict_t[char]+=1

            # return dict_t == dict_s


