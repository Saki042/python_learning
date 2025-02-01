#Converting an Integer into Decimals
import decimal
example = 10
print(type(example))
converted_example = decimal.Decimal(example)
print(converted_example)
print(type(converted_example))


#Converting a String of Integers into Decimals
import decimal
example = '12345'
print(type(example))
converted_example = decimal.Decimal(example)
print(converted_example)
print(type(converted_example))