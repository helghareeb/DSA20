# بسم الله الرحمن الرحيم

# Solution One

# def find_character_in(in_str, fchar):
#     res_list = []
#     for idx, char in enumerate(in_str):
#         if char == fchar:
#             res_list.append(idx)

#     return res_list

# in_str = input('Enter the String: ')
# fchar = input('Enter the Character: ')

# print(find_character_in(in_str, fchar))


def find_char_in(in_str, fchar):
    for idx, char in enumerate(in_str):
        if char == fchar:
            yield idx

in_str = input('Enter the String: ')
fchar = input('Enter the Character: ')

print(list(find_char_in(in_str, fchar)))