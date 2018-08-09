class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r_list = []
        keyboard_key_list = ["asdfghjkl", "qwertyuiop", "zxcvbnm"]
        for word in words:
            for item in keyboard_key_list:
                list_item = list(item)
                list_item.extend(list(word.lower()))
                if len(list(set(list_item))) == list(item):
                    r_list.append(word)
                    continue

        return r_list
