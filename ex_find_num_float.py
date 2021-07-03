data="X-hsb-Confidence:0.8475"
#we need to look for PATTERN
find_start=data.find(':')
find_number=data[find_start+1:]
make_float_find_number=float(find_number)
#print(find_number)
print(make_float_find_number)