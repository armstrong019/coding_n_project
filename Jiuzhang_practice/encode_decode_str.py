class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return None
        if strs == [""]:
            return ""
        x = chr(258).join(strs)
        return x

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s is None:
            return None
        if s == "":
            return [""]
        res = s.split(chr(258))
        return res
