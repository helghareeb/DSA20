# بسم الله الرحمن الرحيم

def mario_pyramid(mmax):
    for i in range(1, mmax + 1):
        print(' ' * (mmax - i), '*' * i)


mario_pyramid(4)