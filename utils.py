import re


def validate(number: str = None) -> str:
    """
    Function to validate a bulgarian phone number
    :param number: string
    :return: valid phone number string format
    """
    # pattern for first case 0878123456
    pattern_one = "([0]{1})?([87-89]{2})?([2-9]{1})?([0-9]{6})"
    # pattern for second case (+)(00)359878123456
    pattern_tow = "(?:(00|\+)([3]{1}[5]{1}[9]{1})?([87-89]{2})?([2-9]{1})?([0-9]{6}))"

    compile_one = re.compile(pattern_one)
    compile_two = re.compile(pattern_tow)

    first_case = compile_one.fullmatch(number)
    second_case = compile_two.fullmatch(number)

    if first_case:
        return "+359{}".format(first_case.group(0)[1:])

    if second_case:
        if second_case.group(1) == '00':
            return "+{}".format(second_case.group(0)[2:])
        else:
            return second_case.group(0)


def sort_data(data, index=None):
    """
    Function to sorted by name
    :param data: list(list(), list())
    :param index: int
    :return: ordered list
    """
    if not index:
        return sorted(data, key=lambda x: x[0])
    else:
        return sorted(data, key=lambda x: x[index], reverse=True)


def print_contact(contact_info, top=False):
    """
    Function to print contact
    :param contact_info: dictionary
    :param top: boolean
    :return: A formatted string for the console
    """
    if not top:
        print("{0[name]:<30} {0[phone]:>30}".format(contact_info))
    else:
        print("{0[name]:<30} {0[phone]:20} {0[outgoing]:>20}".format(contact_info))
