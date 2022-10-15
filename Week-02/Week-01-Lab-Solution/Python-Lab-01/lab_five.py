# بسم الله الرحمن الرحيم

def convert_list_to_dict(str_list):
    result = {}
    for str_item in str_list:
        if str_item[0] not in result.keys():
            result[str_item[0]] = [str_item]
        else:
            result[str_item[0]].append(str_item)
    
    return result

print(convert_list_to_dict(['ahmed', 'amera', 'omar', 'amro', 'hesham', 'mazen']))

