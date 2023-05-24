"""
You will be given a number and you will need to return it as a string in Expanded Form.
"""


def expanded_form(num: int) -> str:
    list_of_numbers = []
    while num > 0:
        list_of_numbers.append(num % 10)
        num = num // 10
    list_of_expanded_form = []
    for i, number in enumerate(list_of_numbers[::-1]):
        list_of_expanded_form.append(number * 10 ** len((list_of_numbers[::-1])[(i + 1):]))
    return " + ".join(str(numb) for numb in list_of_expanded_form if numb != 0)


def test_expanded_form():
    assert expanded_form(123) == "100 + 20 + 3"
    assert expanded_form(7) == "7"
    assert expanded_form(42) == "40 + 2"
    assert expanded_form(90000) == "90000"
    assert expanded_form(777) == "700 + 70 + 7"

    print("Tests passed!")


if __name__ == '__main__':
    test_expanded_form()
