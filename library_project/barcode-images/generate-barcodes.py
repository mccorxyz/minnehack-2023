#!/usr/bin/python3

"""
Use this script to create a barcode to use for library card codes
"""

from barcode import EAN13
from barcode.writer import SVGWriter

m_barcode = input("Enter number for barcode: ").rjust(12, "0")

with open(str(m_barcode) + ".svg", "wb") as f:
    EAN13(str(m_barcode), writer=SVGWriter()).write(f)