# Encryption

Reference 

- pgp: [https://en.wikipedia.org/wiki/Pretty_Good_Privacy](https://en.wikipedia.org/wiki/Pretty_Good_Privacy)
- pyAesCrypt: [https://pypi.org/project/pyAesCrypt/](https://pypi.org/project/pyAesCrypt/)

```py
pip install pyAesCrypt
```

From Python 

```py
import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)
```

Decrypt file test.txt.aes in test.txt:

```
pyAesCrypt -d test.txt.aes
```
