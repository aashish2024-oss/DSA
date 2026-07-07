class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""
        s=0
        for ch in str(n):
            if ch!="0":
                x+=ch
                s+=int(ch)
        if x=="":
            return 0
        return int(x)*s
       
        