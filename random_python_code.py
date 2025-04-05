import array,numpy

# Three different DATA TYPEs:
standard_py_list=[1,2,3,4,5]
array_list=array.array('i',standard_py_list)
numpy_array_list=numpy.array(standard_py_list)
# print(type(array_list))
# print(type(numpy_array_list))

print(numpy.mean(numpy_array_list))
print(numpy.std(numpy_array_list))

# sum=0
# for i in standard_py_list:
#     total=len(standard_py_list)
#     sum +=i
# print(sum/total)