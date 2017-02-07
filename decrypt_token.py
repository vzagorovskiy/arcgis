# Decrypt arcgis tokens
# http://sainsb.github.io/2012/07/18/decrypting-arcgis-server-tokens/
# Python 2.7

from base64 import *

from Crypto.Cipher import AES


def decrypt_token(token, shared_key):
    iv = '\x01' + '\x02' + '\x03' + '\x04' + '\x05' + '\x06' + '\x07' + '\x08' + '\x09' + '\x0A' + '\x0B' + '\x0C' + '\x0D' + '\x0E' + '\x0F' + '\x10'
    if token[-1] != '=': token += '='
    token = b64decode(token, '-_')
    mode = AES.MODE_CBC
    # for portal https://domain.com/portal/portaladmin/security/tokens
    # for server https://domain.com/arcgis/admin/security/tokens
    key = shared_key[:16]
    cipher = AES.new(key, mode, iv)
    return cipher.decrypt(token)


if __name__ == '__main__':
    shared_key = raw_input('Shared key: ')
    token = raw_input('Token: ')
    info = decrypt_token(token, shared_key)
    print(info)
