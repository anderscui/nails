# coding=utf-8
import random
import string


def random_string(n=5):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))


if __name__ == '__main__':
    print(random_string())
