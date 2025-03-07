class Solution(object):
    def getDict(self, str, start, end):
        i = start

        dct = {}
        while (i < end):
            if (str[i] in dct):
                dct[str[i]] += 1
            else:
                dct[str[i]] = 1
            i += 1

        return dct

    def comparedict(self, d1, d2):

        # print("comparing", d1, d2)

        for key in d1:
            if key in d2 and d2[key] == d1[key]:
                # all good
                blank = ""
            elif (d1[key] == 0):
                blank = ""
            else:
                return False

        return True


    
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if (len(p) > len(s)):
            return []

        basedict = self.getDict(p, 0, len(p))

        # print(basedict)

        endl = []

        runningdict = self.getDict(s, 0, len(p))

        # print("start", runningdict)

        i = 0
        while (i < len(s)-len(p)+1):

            # print("before", i, runningdict)

            if (self.comparedict(runningdict, basedict)):
                endl.append(i)

            runningdict[s[i]] -= 1
            
            if (i < len(s)-len(p)):
                if (s[i+len(p)] in runningdict):
                    runningdict[s[i+len(p)]] += 1
                else:
                    runningdict[s[i+len(p)]] = 1
                

            # print("after", i, runningdict)


            i += 1

        return endl
