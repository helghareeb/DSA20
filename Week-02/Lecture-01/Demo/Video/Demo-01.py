def outer_fn():
    print('I am the outer function')

    def inner_fn():
        print('I am the inner function')

    #inner_fn()



#outer_fn()


outer_fn().inner_fn()
