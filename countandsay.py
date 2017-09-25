class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        prev = "1"
        h = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5",
            6:"6", 7:"7", 8:"8", 9:"9", 0:"0"}
        for i in xrange(0, n-1):
            next_ = ""
            j = 0
            while(j < len(prev)):
                char_count = 1
                while(j < len(prev) - 1 and prev[j] == prev[j+1]):
                    char_count += 1
                    j += 1
                next_ += h[char_count]
                next_ += prev[j]
                j += 1
            prev = next_
            print(next_)

if __name__ == '__main__':
    Solution().countAndSay(4)
