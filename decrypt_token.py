# Decrypt arcgis tokens
# http://sainsb.github.io/2012/07/18/decrypting-arcgis-server-tokens/
from Crypto.Cipher import AES
from base64 import *

iv =  '\x01'+ '\x02'+ '\x03'+ '\x04'+ '\x05'+ '\x06'+ '\x07'+ '\x08'+'\x09'+ '\x0A'+ '\x0B'+ '\x0C'+ '\x0D'+ '\x0E'+ '\x0F' + '\x10'
token = 'YOUR_TOKEN'
if token[-1]<>'=':
    token = token + '='
token = b64decode(token, '-_')
mode = AES.MODE_CBC
key = 'YOUR_SHARED_KEY' 
# for portal https://domain.com/portal/portaladmin/security/tokens
# for server https://domain.com/arcgis/admin/security/tokens
key = key [:16]
cipher = AES.new(key, mode, iv)
print(cipher.decrypt(token))
