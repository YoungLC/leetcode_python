class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word==word.lower() or word == word.upper() or word ==str(word[0].upper())+str(word[1:].lower()):
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().detectCapitalUse("Leetcode")