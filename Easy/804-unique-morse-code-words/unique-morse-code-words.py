class Solution:
    def uniqueMorseRepresentations(self, words):
        ma = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.",
              "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        for w in words:
            t = ''.join([ma[ord(x) - ord('a')] for x in w])
            res.add(t)
        return len(res)
