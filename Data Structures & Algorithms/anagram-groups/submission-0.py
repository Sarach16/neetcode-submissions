class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for stri in strs:
            count = [0]*26
            for char in stri:
                count[ord(char)-97]+=1
            my_dict[tuple(count)].append(stri)
        return list(my_dict.values())

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  #    #Brute Force
    #    #create a dictionary for every string
    #    #create an array of disctionaries 
    #    #compare each dictionary with all the others using nested loops
    #    my_dicts={}
    #    for i, stri in enumerate(strs):
    #         if stri not in 
    #         my_dicts.append({})
    #         for char in stri:
    #             if char not in my_dicts[i]:
    #                 my_dicts[i][char]=1
    #             else:
    #                 my_dicts[i][char]+=1
        
    #     #Now we should have a list made up of a dictionary corresponding
    #     #to the frequency of every char in the list
 
        
