class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<2:
            return True
        if not word[1:].islower() and not word[1:].isupper():
            return False
        elif word[0].islower() and word[1:].isupper():
            return False
        else:
            return True
            