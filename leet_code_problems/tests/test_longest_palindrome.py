import unittest
from longest_palindrome import Solution


class TestLongestPalindrome(unittest.TestCase):
    def test_longest_palindrome(self):
        sol = Solution()

        assert sol.longestPalindrome('babad') == 'bab' or 'aba'
        assert sol.longestPalindrome('cbbd') == 'bb'
        assert sol.longestPalindrome('dd') == 'dd'
        assert sol.longestPalindrome('a') == 'a'
        assert sol.longestPalindrome('ac') == 'a' or 'c'
        assert sol.longestPalindrome('racecar') == 'racecar'
        assert sol.longestPalindrome((
            'nmxyncuzlwhiobggiowtjexyzbzyhuqmpnyyimazcrnhrnkydxnioqhtchnnoqhuezypyx'
            'iepdvyesihlvbuzctptsaowfllxfdqvbwyitsegpbarqqpcrrvemwkglouhhtuxjdeppatd'
            'iiwhwvrqxqjcmzhuwurlqrshlsjyxksfjmhykyhcbpmrbsmbrrjwndjsgqdrafidmelnobh'
            'tpblozbzttpzheeffwysfrrwtewjnmqoyrvfxmgcmdoadagatwyocixggwppnmtrnfrbiij'
            'wojpetuqwknvtqgspuogrbqqptsrljjiaalmqlchlszflyixxpnkttzbrvhzrjzfbpuquuy'
            'zwhattxvoqpzieguwvmlrggrlmvwugeizpqovxttahwzyuuqupbfzjrzhvrbzttknpxxiyl'
            'fzslhclqmlaaijjlrstpqqbrgoupsgqtvnkwqutepjowjiibrfnrtmnppwggxicoywtagad'
            'aodmcgmxfvryoqmnjwetwrrfsywffeehzpttzbzolbpthbonlemdifardqgsjdnwjrrbmsb'
            'rmpbchykyhmjfskxyjslhsrqlruwuhzmcjqxqrvwhwiidtappedjxuthhuolgkwmevrrcpq'
            'qrabpgestiywbvqdfxllfwoastptczubvlhiseyvdpeixypyzeuhqonnhcthqoinxdyknrh'
            'nrczamiyynpmquhyzbzyxejtwoiggboihwlzucnyxmn'))


if __name__ == '__main__':
    unittest.main()
