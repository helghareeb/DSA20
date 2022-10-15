# بسم الله الرحمن الرحيم

vowels = ['a', 'e', 'i', 'o', 'u']

def remove_vowels(in_str):
    out_str = ''
    for i in in_str:
        if i not in vowels:
            out_str += i  
    return out_str

def list_iterator(str_list):
    res = []
    for in_str in str_list:
        res.append(remove_vowels(in_str))
    return res

# in_str = input('Enter a word: ')
in_str = ['mobile', 'cloud', 'javascript', 'huawei']
print(list_iterator(in_str))