# بسم الله الرحمن الرحيم

def do_math(*args, **kwargs):
    # for key in kwargs:
    #     if key == 'operation':
    if kwargs['operation'] == 'add':
        result = 0
        for arg in args:
            result += arg
        return result
    elif kwargs['operation'] == 'mul':
        result = 1
        for arg in args:
            result *= arg
        return result
    else:
        raise NameError
