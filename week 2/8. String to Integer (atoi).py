class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lstrip()

        newstr = ""

        mult = 1

        print(s)

        i = 0
        while (i < len(s)):
            if (s[i] == "-" and i == 0):
                mult = -1
            elif (s[i] == "+" and i == 0):
                mult = 1
            elif (not s[i] in "1234567890"):
                break
            else:
                newstr += s[i]

            i += 1

        print(newstr)

        if (newstr == ""):
            return 0

        
        newint = int(newstr)*mult

        if (newint < -(2**31)):
            newint = -(2**31)
        if (newint > 2**31-1):
            newint = 2**31-1


        return newint
