import unittest
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        cnt = len(s)
        hash_str = {}
        for i in range(256):
            hash_str[chr(i)] = 0
        print(hash_str)
        i = 0
        j = 0
        max_length = 0
        while(j<cnt):
            if hash_str[s[j]] == 1:
                max_length = max(j-i,max_length)
                while(s[i]!=s[j]):
                    hash_str[s[i]] = 0
                    i+=1
                i+=1
                j+=1
            else:
                hash_str[s[j]] = 1
                j+=1
        max_length = max(max_length,cnt-i)
        return max_length

class TestSolution(unittest.TestCase):
    def setUp(self):
        print('haha')
        pass
    def tearDown(self):
        pass
    def test_Case1(self):
        Test = Solution()
        string = "abcabcbb"
        max_length = Test.lengthOfLongestSubstring(string)
        print(max_length)
        self.assertEqual(max_length,3)

if __name__ == '__main__':
    unittest.main()
            
    Test = Solution()
    string = "abcabcbb"
    max_length = Test.lengthOfLongestSubstring(string)
    print('max_length = ',max_length)
    
    string = "pwwkew"
    max_length = Test.lengthOfLongestSubstring(string)
    print('max_length = ',max_length)
