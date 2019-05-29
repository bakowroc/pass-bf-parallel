import itertools
import string


def generate_strings(length=4):
    chars = string.ascii_letters + string.digits
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)
