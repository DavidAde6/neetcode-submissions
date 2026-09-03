class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "no string"
        return "~".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "no string":
            return []
        return s.split("~")