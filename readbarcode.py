# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import cv2
import numpy as np
from reportlab.graphics.barcode import createBarcodeImageInMemory
from pyzbar.pyzbar import decode

# https://docs.reportlab.com/reportlab/userguide/ch1_intro/
# https://docs.reportlab.com/reportlab/barcode/
# https://pypi.org/project/opencv-python/
# https://numpy.org/doc/stable/
# https://pypi.org/project/pyzbar/

# Barcode Types: 
#     EAN8, EAN13, EAN5, ISBN, UPCA, QR, Code128, Code128Auto
#     Standard39, Standard93, MSI, Codebar, Code11, FIM, POSTNET
#     Extended39, Extended93, I2of5, ECC200DataMatrix

#  you can also review my previous example:
# https://github.com/xdevsoft/barcodegen
barcode = createBarcodeImageInMemory(
    'Code128',                  # Refer to barcode types 
    value='123456789',          # code to be encoded/printed
    width=400, 
    height=100,
    format='png'                # png, gif, tiff
)

# convert the binary image to numpy array
nparr = np.frombuffer(barcode, dtype=np.uint8)
# then need to convert it to cv image
img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

# It can read multiple barcode on a single image
for d in decode(img):   # decode the image
    print(d.data.decode('utf-8'), d.type)
