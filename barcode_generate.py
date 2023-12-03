from barcode import EAN13
from bardcode.writer import ImageWriter
numer: 14817461219
my_code = EAN13(number, writer=ImageWriter())
my_code.save("barcode")
