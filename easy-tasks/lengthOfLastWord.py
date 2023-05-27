"""Given a string s consisting of words and spaces, return the length of the last word in the string."""


class Solution(object):

    @staticmethod
    def length_of_last_word(s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0:
            return len(s.split()[-1])
        return 0


def test_length_of_last_word():
    assert Solution.length_of_last_word("Hello World") == 5
    assert Solution.length_of_last_word("The quick brown fox") == 3
    assert Solution.length_of_last_word("OpenAI is amazing") == 7
    assert Solution.length_of_last_word("ChatGPT") == 7
    assert Solution.length_of_last_word("Python") == 6
    assert Solution.length_of_last_word("") == 0
    assert Solution.length_of_last_word("Testing") == 7
    assert Solution.length_of_last_word("This    is    a    test") == 4

    print("Test passed!")


if __name__ == '__main__':
    test_length_of_last_word()
