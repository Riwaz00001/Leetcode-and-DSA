class Solution(object):
    def commonChars(self, words):
        reference=Counter(words[0])
        for word in words:
            reference&=Counter(word)
        return list(reference.elements())