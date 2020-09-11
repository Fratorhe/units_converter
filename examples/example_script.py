from units_converter import convert_units

to_convert = '3 meter per second'
new_units = 'km per hour'

converted = convert_units(to_convert, new_units)
print(converted)