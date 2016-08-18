import re
s = "bob sue jon richard harry"
r = re.compile('(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)')
[m.groupdict() for m in r.finditer(s)]
[{'name2': 'sue', 'name': 'bob'}, {'name2': 'richard', 'name': 'jon'}]


def words(input):
    rgx = re.compile("(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    return [m.groupdict() for rgx in rgx.finditer(input)]


def phone_number(input):
    rgx = re.compile("(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    return [m.groupdict() for rgx in rgx.finditer(input)]


def money(input):
    rgx = re.compile("(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    return [m.groupdict() for rgx in rgx.finditer(input)]


def zipcode(input):
    rgx = re.compile("(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    return [m.groupdict() for rgx in rgx.finditer(input)]


def date(input):
    rgx = re.compile("(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    return [m.groupdict() for rgx in rgx.finditer(input)]


# ADVANCED MODE
def address(input):
    rgx = re.compile("(?P<name>[a-z]+)\s+(?P<name2>[a-z]+)")
    return [m.groupdict() for rgx in rgx.finditer(input)]
