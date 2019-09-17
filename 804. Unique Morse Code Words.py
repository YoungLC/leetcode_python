class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result_list = []
        alph_map = {
            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
            "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
            "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
            "x": "-..-", "y": "-.--", "z": "--.."}
        for item in words:
            morse_str = ""
            for i in item:
                morse_str += alph_map[i]
            result_list.append(morse_str)
        print result_list
        return len(list(set(result_list)))


if __name__ == '__main__':
    input = ["gin", "zen", "gig", "msg"]
    print Solution().uniqueMorseRepresentations(input)
