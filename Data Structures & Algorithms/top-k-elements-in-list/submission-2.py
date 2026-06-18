class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #the max a number can be repeated is the length of the string
        #bucketsort ??
        buckets = [ [] for _ in range(len(nums) + 1)]

        #dictionay that maps number to it count
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for num, count in seen.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets) -1 , 0, -1):
            for num in buckets[i]:
                result.append(num)
                k -=1
                if k == 0:
                    return result
            

        

        
  
            



 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        
        
        





        
        
        
        # count ={}
        # list_freq = [[]for i in range(len(nums)+1)]

        # for n in nums:
        #     count[n]= 1 + count.get(n,0)
        # for n,c in count.items():
        #     list_freq[c].append(n)
        
        # res=[]
        # for i in range(len(list_freq)-1,0,-1):
        #     for n in list_freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # #loop through the array while adding element to dict and counting
        # dict_freq = {}
        # for num in nums:
        #     if num in dict_freq:
        #         dict_freq[num]+=1
        #     else:
        #         dict_freq[num]=1
        
        # # find the k largest values of the dict
        # #creat an list of size k
        # list_freq = [0]*k
        # #loop through dictionary and find max value
        # for i in range(len(list_freq)):
        #     key = next(j for j,v in dict_freq.items() if v == max(dict_freq.values()))
        #     list_freq[i]=key
        #     del dict_freq[key]

        # return list_freq

            
        # append the key of max value to list
        # delete key from dictionary 
        # loop again until k list is full

        # return the list
