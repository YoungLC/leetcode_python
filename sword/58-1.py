class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # tmp = ""
        # res = []
        # s = s.strip()
        # for i in range(len(s)):
        #     if s[i]:
        #         if not tmp and s[i] is " ":
        #             continue
        #         tmp += s[i]
        #         if " " in tmp:
        #             res.append(tmp.strip())
        #             tmp = ""
        #         elif i == len(s) - 1:
        #             res.append(tmp)
        #             tmp = ""
        # print res,len(res)
        # return " ".join(set(res[::-1])).strip()
        s=s.strip()
        res= s.split(" ")
        res =[x for x in res if x]
        print res
        return " ".join(res[::-1]).strip()



if __name__ == '__main__':
    s = "a good   example"
    print(Solution().reverseWords(s))
