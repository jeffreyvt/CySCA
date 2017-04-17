# CySCA

## Cracking the RSA
This is a Common Factor Attack for RSA encrypted messages <br/>
Install the following dependencies for python3:
```
pip3 install pycrypto
pip3 install pyasn1
```
There might be more dependencies... i donno...... <br/>
Run the python3 file [here](RSA/100%20RSA%20challenge/main.py)

## Decrypting the RSA encrypted messages
After obtaining the private key from the previous code, run the following command in the terminal.
```
openssl rsautl -decrypt -inkey <private key> -in <cipher text> -out <output text>
```
for example
```
openssl rsautl -decrypt -inkey key7.pem -in 7.bin -out plaintext7.txt
```
