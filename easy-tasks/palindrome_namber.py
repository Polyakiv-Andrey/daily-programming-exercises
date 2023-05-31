"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:

    @staticmethod
    def is_palindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]


def test_is_palindrome():
    assert Solution.is_palindrome(121) is True
    assert Solution.is_palindrome(12321) is True
    assert Solution.is_palindrome(1221) is True
    assert Solution.is_palindrome(123) is False
    assert Solution.is_palindrome(123456) is False
    assert Solution.is_palindrome(987654) is False

    print("Test passed!!")


if __name__ == '__main__':
    test_is_palindrome()
