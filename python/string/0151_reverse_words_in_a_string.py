# LeetCode 151: Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed list of words into a single string with spaces
        return ' '.join(reversed_words)
