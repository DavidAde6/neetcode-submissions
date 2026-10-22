class Solution:
    def isValid(self, s: str) -> bool:
        # 2 pointers at each end, nah
        #(){}
        # ({()}([]))
        comp = []
        for c in s:
            if c == "(":
                comp.append(")")
            elif c == "{":
                comp += ("}")
            elif c == "[":
                comp += ("]")
            elif not comp or c != comp.pop():
                return False

        return not comp
