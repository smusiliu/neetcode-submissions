class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g_dict = {}

        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in g_dict:
                g_dict[x].append(strs[i])
            else:
                g_dict[x] = [(strs[i])]

        return list(g_dict.values())
        
        