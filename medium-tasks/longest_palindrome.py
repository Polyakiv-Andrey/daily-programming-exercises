"""Given a string s, return the longest palindromic substring in s."""


class Solution(object):

    @staticmethod
    def longest_palindrome(s):
        """
        :type s: str
        :rtype: str
        """
        palindromes = []
        length_of_palindromes = []
        for left_index, left_letter in enumerate(s):
            for right_index, right_letter in enumerate(s[::-1]):
                right_index = len(s) - 1 - right_index
                if right_index <= left_index:
                    break
                if right_letter == left_letter:
                    if right_index == len(s) - 1:
                        palindrome = s[left_index:]
                    else:
                        palindrome = s[left_index:right_index + 1]
                    if palindrome == palindrome[::-1]:
                        palindromes.append(palindrome)
                        length_of_palindromes.append(len(palindrome))
        if not palindromes:
            return s[0]
        index = length_of_palindromes.index(max(length_of_palindromes))
        return palindromes[index]


def test_longest_palindrome():
    assert Solution.longest_palindrome("babad") == "bab"
    assert Solution.longest_palindrome("cbbd") == "bb"
    assert Solution.longest_palindrome("a") == "a"
    assert Solution.longest_palindrome("abcdefg") == "a"
    assert Solution.longest_palindrome("racecar") == "racecar"
    assert Solution.longest_palindrome("abbabbabba") == "abbabbabba"
    assert Solution.longest_palindrome("ab") == "a"
    assert Solution.longest_palindrome("abcde") == "a"

    print("All test cases passed!")


if __name__ == '__main__':
    test_longest_palindrome()
