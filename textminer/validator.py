import re


def binary(text):
    return re.match(r"^[0-1]+$", text)


def binary_even(text):
    return re.match(r"^[0-1]+0$", text)


def hex(text):
    return re.match(r"^[a-fA-F0-9]+$", text)


def word(text):
    return re.match(r"^[\w]*[-]*[a-zA-z]+$", text)


def words(text, count=None):
    words = re.findall(r"[\w]*[-]*[a-zA-z]+", text)
    if count:
        return len(words) == count
    else:
        return len(words) == len(text.split(" "))


def phone_number(text):
    return re.match(r"^\(*\d{3}\)*[\s.-]*\d{3}[\s.-]*\d{4}$", text)


def money(text):
    return re.match(r"^\$[0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?$", text)


def zipcode(text):
    return re.match(r"^\d{5}(\-\d{4})*$", text)


def date(text):
    return re.match(r"^\d{1,4}[/-]\d{1,4}[/-]\d{1,4}$", text)


# ADVANCED
def advanced_date(text):
    pass


def email(text):
    return re.match(r"^.+@[a-zA-Z]+\.[a-zA-Z]{2,3}$", text)


def address(text):
    return re.match(
                r"\A\d+\s[\w\s\.]+(\n|,)[\w\s]+,\s[A-Z]{2}\s\d{5}[-\d{4}]*\Z",
                text)
