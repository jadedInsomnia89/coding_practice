import unittest
from longest_substr_wo_repeating_chars import Solution


class TestAddLinkedLists(unittest.TestCase):
    def test_length_of_longest_substring(self):
        sol = Solution()

        self.assertEqual(sol.lengthOfLongestSubstring(''), 0)
        self.assertEqual(sol.lengthOfLongestSubstring(' '), 1)
        self.assertEqual(sol.lengthOfLongestSubstring('z'), 1)
        self.assertEqual(sol.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(sol.lengthOfLongestSubstring('au'), 2)
        self.assertEqual(sol.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(sol.lengthOfLongestSubstring('pwwkew'), 3)
        

if __name__ == '__main__':
    unittest.main()
