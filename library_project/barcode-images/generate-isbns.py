#!/usr/bin/python3

"""
This script will generate ISBN barcodes from the raw numbers.
"""

from barcode import ISBN13
from barcode.writer import SVGWriter

m_barcode = input("Enter number for ISB13: ")

# Or to an actual file:
with open(str(m_barcode) + ".svg", "wb") as f:
    ISBN13(str(m_barcode), writer=SVGWriter()).write(f)