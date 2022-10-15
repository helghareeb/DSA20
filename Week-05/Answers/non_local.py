# بسم الله الرحمن الرحيم

name = 'Ahmed'

def outer_fn():
    # global name 
    name = 'Ali'
    def inner_fn():
        # global name
        nonlocal name
        print(name) # Ali
        name = 'Sara'
        print(name) # Sara
    inner_fn()
    print(name) # Sara

print(name) # Ahmed
outer_fn()
print(name) # Ahmed

# def inner_fn():
#     nonlocal name
#     name = 'Ali'