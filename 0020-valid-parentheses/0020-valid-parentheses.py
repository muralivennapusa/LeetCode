class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        p={
            ')':'(',
            '}':'{',
            ']':'['
        }
        # c={
        #     '(':')',
        #     '{':'"',
        #     '[':']'
        # }
        for i in s:
            if i in '({[':
                l.append(i)
            elif i in ')}]' and len(l)==0:
                return False
            elif p[i]!=l[-1]:
                return False
            else:
                l.pop()
        return True if len(l)==0 else False