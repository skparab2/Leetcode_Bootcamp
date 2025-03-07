class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        splt = s.split(" ")

        i = len(splt)-1

        finstr = ""

        while (i >= 0):

            fd = splt[i]

            # print("<"+fd+">")

            if (fd != " " and fd != ""):

                fd = fd.lstrip()
                fd = fd.rstrip()



                finstr += fd

                if (i != 0):
                    finstr += " "

            i -= 1
        
        finstr = finstr.lstrip()
        finstr = finstr.rstrip()

        return finstr
