import random
import string


def new_url(size=6, char=string.ascii_letters + string.digits):
    return ''.join(random.choice(char) for _ in range(size))
