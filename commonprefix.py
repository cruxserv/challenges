class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pfx = ""
        for i in range(len(strs[0])):
            for w in strs:
                if i == len(w) or w[i] != strs[0][i]:
                    return pfx
            pfx += strs[0][i]
