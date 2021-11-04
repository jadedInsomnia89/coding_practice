class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res

        # if len(s) == 0:
        #     return 0
        
        # i = 0
        # j = 1
        # long_sub = ''
        # temp_sub = ''
        # while i < len(s):
        #     temp_sub = s[i]
            
        #     while j < len(s):
        #         if s[j] not in temp_sub:
        #             temp_sub += s[j]
        #         else:
        #             break
        #         j += 1
                
        #     if len(long_sub) < len(temp_sub):
        #         long_sub = temp_sub
            
        #     i += 1
        #     j = i + 1

        # return len(long_sub)
