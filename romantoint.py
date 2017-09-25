class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # MMMCMXCIX    
        num = 0
        h = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        if len(s) == 1:
            return h[s[0]]    
        for i in range(len(s)-1):
            if h[s[i]] >= h[s[i+1]]:
                num += h[s[i]]
            else:
                num -= h[s[i]]
        num += h[s[i+1]]
        return num
        