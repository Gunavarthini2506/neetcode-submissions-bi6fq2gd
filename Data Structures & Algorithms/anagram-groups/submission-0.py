class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a={}
        for word in strs:
            key="".join(sorted(word))
            if key in a:
                a[key].append(word)
            else:
                li=[]
                li.append(word)
                a[key]=li
        return list(a.values())
