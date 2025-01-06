class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x for x in s.lower() if x in "1234567890qwertyuiopasdfghjklmnbvcxz"]
        return s==s[::-1]
        