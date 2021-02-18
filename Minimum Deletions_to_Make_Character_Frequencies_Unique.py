# A string s is called good if there are no two different characters
# in s that have the same frequency.
#
# Given a string s, return the minimum number of characters you
# need to delete to make s good.
#
# The frequency of a character in a string is the number of times
# it appears in the string. For example, in the string "aab", the
# frequency of 'a' is 2, while the frequency of 'b' is 1.
#
# Example1:
#
# Input: s = "aab"
# Output: 0
# Explanation: s is already
# good.
#
# Example 2:
#
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
#
# Example 3:
#
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the
# end (i.e. frequency of 0 is ignored).


import collections


class Solution:
    def minDeletions(self, s):
        dict = collections.Counter(s)

        values = sorted(dict.values(), reverse=True)
        count = 0
        seen = set()

        for num in values:

            while num in seen and num != 0:
                count += 1
                num -= 1

            seen.add(num)

        return count