from quantulum3 import parser
from pint import UnitRegistry
from pint.errors import DimensionalityError


def convert_units(text_with_units, new_units=None):
	# this is the main function to convert units. 
	ureg = UnitRegistry()

	# is no new units are provided, let's just change to SI units
	if new_units is None:
		new_units = 'SI'

	# separate number and units for the input
	value, unit = get_value_unit(text_with_units)
	print(f'The original units are: {unit}')
	print(unit)
	# parse it in Pint
	dimensioned_number = value * unit

	# If new units is SI, just move the basis units. 
	if new_units == 'SI':
		return dimensioned_number.to_base_units()
	else: 
		# otherwise, we first add a 1 to the units (because normally they do not have a number)
		# this is only to make it easier for quantulum. 
		if not new_units[0].isdigit():
			new_units = '1.0 '+ new_units
		# we drop the value, but get the units, from quantulum or pint
		_, new_unit = get_value_unit(new_units)

		# we try to change to the new units, but it is possible the user made a mistake. 
		try: 
			number_with_new_units = dimensioned_number.to(new_unit)
			print(f'In the new units: {number_with_new_units}')
		except DimensionalityError:
			number_with_new_units = 'error with units'
		return number_with_new_units

def get_value_unit(quantity_with_units):
	ureg = UnitRegistry()
	# this function separates the quantity and the units
	# if only units are provided, it returns a 1 for the value. 
	try: # to parse using quantulum
		parsed_units = parser.parse(quantity_with_units)[0]

		value = parsed_units.value # get the value
		num_units_quantulum = parsed_units.surface

		# if the first position in the string is a digit means we have a number with units. Otherwise, only the units.
		if num_units_quantulum[0].isdigit():
			unit = ' '.join(num_units_quantulum.split()[1:]) # take only the units (remove the number)
		else:
			unit = num_units_quantulum # there is no number in this case
		unit = ureg.parse_expression(unit)
	except: 
		print('Using Pint')
		# if quantulum fails, we try to parse using pint
		unit = ureg.parse_expression(quantity_with_units)
		value = 1
	return value, unit

if __name__=='__main__':

	convert_units('51 kelvin^2 / second^2', 'kelvin^2 /min^2')
