class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        sorted_dic=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
        lst=[]
        for i in range(k):
            lst.append(list(sorted_dic.keys())[i])
        return lst    