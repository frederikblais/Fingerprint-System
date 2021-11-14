import time
from pyfingerprint.pyfingerprint import PyFingerprint

# ------------------
# ENROLL FINGERPRINT
# ------------------

## Initialize sensor
try:
    f = Pyfingerprint('/dev/ttyUSB0', 9600, 0xFFFFFFFF, 0x00000000)

    if( f.verifyPassword() == False ):
        raise ValueError('The given password is incorrect.')

except Exception as e:
    print('The sensor could not be initialized.')
    print('Error: ' + str(e))
    exit(1)

## Get sensor data
print('Current used template: ' + str(f.getTemplateCount()) + '/' +
        str(f.getStorageCapacity()))
