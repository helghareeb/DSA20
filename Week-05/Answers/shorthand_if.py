# بسم الله الرحمن الرحيم

# shorthand if

def temp_in_word(temp):
    if temp > 100:
        return 'Hot'
    # elif 25 < temp < 100:
    #     return 'Intermediate'
    else:
        return 'Cold' 

# result = temp_in_word(101)
temp = 101
# print(result)

sh_result = 'Hot' if temp > 100 else 'Cold'
print(sh_result)
