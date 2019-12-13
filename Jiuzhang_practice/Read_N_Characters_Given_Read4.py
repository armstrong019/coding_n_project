class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_4 = ['']*4 # this buff is assigned to read4
        t = n//4 # the integer part
        resi = n%4 # the residual part
        p0 = 0 # pointer that records the position of the next letter
        for i in range(t):
            val = read4(buf_4)
            buf[p0:p0+val] = buf_4
            p0+=val
            if val<4: # this case all data in the string has been read
                return p0 # p0 is the number of the actual charactor read

        # this part is for the residual part
        val = read4(buf_4)
        ind = min(val, resi) # the actual number of letters we need is the minimum of the two.
        buf[p0:p0+ind] = buf_4
        p0 = p0+ind
        return p0

# this question is a easy one. Need to think about how to handle corner cases.


