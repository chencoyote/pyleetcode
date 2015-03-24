'''
answer
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        s = 0
        while n is not 0:
            if n % 2 == 1:
                s += 1
            n /= 2
        return s

'''
resolving 
'''

def hammingWeight(n):
    s = 0
    while n is not 0:
        if n % 2 == 1:
           s += 1
        print "n: ", n
        n /= 2
        # n = n >> 1
    return s
q = 0x10111011011 # count 8 1-bits
print bin(q)
print hammingWeight(q)


