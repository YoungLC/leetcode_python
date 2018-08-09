class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000
                     }
        result = 0
        for i in range(0, len(s)):
            value = roman_map[s[i]]
            if i == len(s) - 1 or roman_map[s[i + 1]] <= roman_map[s[i]]:
                result += value
            else:
                result -= value
        return result


if __name__ == '__main__':
    print Solution().romanToInt("IV")
