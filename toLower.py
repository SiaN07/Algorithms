class Solution:
    def toLowerCase(string): 
        res = []
        for c in string:
            char = c
            if c >='A' and c <='Z':
                char = chr(ord(c)+32)
            res.append(char)
        return "".join(res)
    print(toLowerCase("tTh cTRYw"))
