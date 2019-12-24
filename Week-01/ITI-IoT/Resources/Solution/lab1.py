# def vowel(w):
#     string = w
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for x in w.lower():
#         if x in vowels:
#             string = string.replace(x,"")
#
#     return string
# s=input('Enter any string ' )
# print(vowel(s))
######################################################################
# n=int(input('Please enter a positive integer : '))
# multi=[[x *z for z in range(1,x+1)]for x in range(1,n+1)]
# print(multi)
#####################################################################
# import math
#
# def area (*args):
# 	if args[0] == "t":
# 		return args[1] * args[2] * 0.5
# 	if args[0] == "r":
# 		return args[1] * args[2]
# 	if args[0] == "s":
# 		return args[1] * args[2]
# 	if args[0] == "c":
# 		return args[1]**2 * math.pi
#
# areaCal = area ("t", 5, 2)
#
# print(areaCal)


############################################################################
# def names (args):
# 	dic = {}
# 	for name in args:
# 		if type(name) is str:
# 			firstLetter = name[0:1].lower()
# 			try:
# 				dic2 = dic.__getitem__(firstLetter)
# 			except:
# 				dic.__setitem__(firstLetter, [name])
# 			else:
# 				dic2.append(name)
# 	return dic
#
#
# s = input ('enter names  ')
# arr=s.split(" ")
# print(arr)
# print(names(arr))
#####################################################################
# x = int(input('enter number of  * :  '))
# for n in [" " * (x - y) + "*" * y for y in range (1, x + 1)]:
# 	print(n)
