"""
def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != "-":
        return False # missing dash
    for i in range (4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != "-":
        return False # missing dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True
"""
"""
Try replacing this block of text with the next block of text.
print('Is 415-555-0000 a phone number?')
print(isPhoneNumber('415-555-0000'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
"""
"""
message = "Call me at 415-555-1011 tomorrow, or at 415-555-9999."
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+ chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
"""

import re
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
#mo = phoneNumRegex.search("Call me at 415-555-1011 tomorrow, or at 415-555-9999.")
#print(mo.group())
print(phoneNumRegex.findall("Call me at 415-555-1011 tomorrow, or at 415-555-9999."))
