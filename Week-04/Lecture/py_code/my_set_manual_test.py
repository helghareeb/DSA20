# بسم الله الرحمن الرحيم

from my_set import MySet

a_courses = MySet()
a_courses.add( "CSCI-112" )
a_courses.add( "MATH-121" )
a_courses.add( "HIST-340" )
a_courses.add( "ECON-101" )

# for course in a_courses:
#     print(course)

print(f'Ahmed: {a_courses}')

h_courses = MySet()
h_courses.add( "POL-101" )
h_courses.add( "ANTH-230" )
h_courses.add( "CSCI-112" )
h_courses.add( "ECON-101" )

print(f'Hesham: {h_courses}')

## print(a_courses - h_courses)
print(f'Intersection: {a_courses.intersect(h_courses)}')
# # print(f'Union: {a_courses.union(h_courses)}')
print(f'Union: {a_courses  + h_courses}')
# print(f'Difference: {a_courses.difference(h_courses)}')
print(f'Difference: {a_courses  - h_courses}')



# c_courses = MySet()
# c_courses.add( "CSCI-112" )
# c_courses.add( "MATH-121" )
# c_courses.add( "HIST-340" )
# c_courses.add( "ECON-101" )
