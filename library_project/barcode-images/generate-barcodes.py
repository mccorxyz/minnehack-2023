#!/usr/bin/python3

from io import BytesIO

from barcode import EAN13
from barcode.writer import SVGWriter

m_barcode = input("Enter number for barcode: ").rjust(12, "0")

# Or to an actual file:
with open(str(m_barcode) + ".svg", "wb") as f:
    EAN13(str(m_barcode), writer=SVGWriter()).write(f)