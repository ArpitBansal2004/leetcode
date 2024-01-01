class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        charset = set()
        li = 0

        for ri in range(n):
            if s[ri] not in charset:
                charset.add(s[ri])
                max_length = max(max_length, ri - li + 1)
            else:
                while s[ri] in charset:
                    charset.remove(s[li])
                    li += 1
                charset.add(s[ri])
        
        return max_length