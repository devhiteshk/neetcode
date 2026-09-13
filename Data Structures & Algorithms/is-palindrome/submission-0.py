class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(s1)//2):
            if s1[i].lower() != s1[len(s1)-1-i].lower():
                return False

        return True