import random

def lotto_number():
    lotto_li = list(range(1,46))
    lotto = sorted(random.sample(lotto_li, 6))
    return lotto