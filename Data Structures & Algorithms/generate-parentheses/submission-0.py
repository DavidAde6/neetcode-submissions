class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if given 0 return nothing
        # thinking

        # dfs(openlength, open, cur):
        # if open is greater than 1, close can be called
        # if openlength equals n, open cant be called
        # end loop when openlength is n and open is 0

        res = []
        ""
        def dfs(openLen, toClose, cur):
            if openLen == n and toClose == 0:
                res.append(cur)
                return
            if openLen < n:
                dfs(openLen + 1, toClose + 1, cur + "(")
            if toClose > 0:
                dfs(openLen, toClose - 1, cur + ")")

        dfs(0, 0, "")
        return res