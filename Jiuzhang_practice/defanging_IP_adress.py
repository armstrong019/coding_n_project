class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new = []
        for i in range(len(address)):
            if address[i] == ".":
                new.append('[.]')
            else:
                new.append(address[i])

        new = ''.join(new)
        return new
