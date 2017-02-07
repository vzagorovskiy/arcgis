# Decrypt arcgis tokens
# http://sainsb.github.io/2012/07/18/decrypting-arcgis-server-tokens/
# Python 2.7

from base64 import b64decode
from Crypto.Cipher import AES
import logging


def decrypt_token(token, shared_key):
    try:
        iv = '\x01' + '\x02' + '\x03' + '\x04' + '\x05' + '\x06' + '\x07' + '\x08' + '\x09' + '\x0A' + '\x0B' + '\x0C' + '\x0D' + '\x0E' + '\x0F' + '\x10'
        if token[-1] != '=':
            token += '='
        token = b64decode(token, '-_')
        mode = AES.MODE_CBC
        key = shared_key[:16]
        cipher = AES.new(key, mode, iv)
        return cipher.decrypt(token)
    except:
        logging.exception('Error occured')


if __name__ == '__main__':
    print('Shared key for portal https://domain.com/portal/portaladmin/security/tokens')
    print('Shared key for server https://domain.com/arcgis/admin/security/tokens')
    shared_key = raw_input('Shared key: ')
    token = raw_input('Token: ')
    info = decrypt_token(token, shared_key)
    if info is not None:
        print(info)
