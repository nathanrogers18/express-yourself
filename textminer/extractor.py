import re


def phone_numbers(text):
    return re.findall(r"\(*\d{3}\)*[\s.-]*\d{3}[\s.-]*\d{4}", text)


def emails(text):
    return re.findall(r"\w*\.*\w+@[a-zA-Z]+\.[a-zA-Z]{2,3}", text)
