class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #loop through the array while adding element to dict and counting
        dict_freq = {}
        for num in nums:
            if num in dict_freq:
                dict_freq[num]+=1
            else:
                dict_freq[num]=1
        
        # find the k largest values of the dict
        #creat an list of size k
        list_freq = [0]*k
        #loop through dictionary and find max value
        for i in range(len(list_freq)):
            key = next(j for j,v in dict_freq.items() if v == max(dict_freq.values()))
            list_freq[i]=key
            del dict_freq[key]

        return list_freq

            
        # append the key of max value to list
        # delete key from dictionary 
        # loop again until k list is full

        # return the list
