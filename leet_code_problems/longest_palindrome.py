class Solution:
    def expand_around_center(self, s: str, l_index: int, r_index: int) -> str:
        while l_index >= 0 and r_index < len(s) and s[l_index] == s[r_index]:
            l_index -= 1
            r_index += 1

        return r_index - l_index - 1


    def longestPalindrome(self, s: str) -> str:
        pal_start = 0
        pal_end = 0

        for i in range(len(s)):
            substr1 = self.expand_around_center(s, i, i)
            substr2 = self.expand_around_center(s, i, i+1)
            long_sub = max(substr1, substr2)

            if long_sub > pal_end - pal_start:
                pal_start = i - (long_sub - 1) // 2
                pal_end = i + long_sub // 2


        return s[pal_start: pal_end+1]


# Brute force method
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         long_pal = s[0]
#         for i in range(len(s) - 1):

#             j = i + 1
#             while j < len(s):
#                 str_to_compare = s[i:j + 1]
#                 reverse_str = str_to_compare[::-1]

#                 if str_to_compare == reverse_str:
#                     if len(str_to_compare) > len(long_pal):
#                         long_pal = str_to_compare
#                 j += 1

#         return long_pal
