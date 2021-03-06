from Crypto.PublicKey import RSA
import math
import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64
from os import listdir
from os.path import isfile, join

def pempriv(n, e, d, p, q, dP, dQ, qInv):
    template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
    seq = pyasn1.type.univ.Sequence()
    for x in [0, n, e, d, p, q, dP, dQ, qInv]:
        seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
    der = pyasn1.codec.der.encoder.encode(seq)
    return template.format(base64.encodebytes(der).decode('ascii'))

def encrypt(m, e, n):
    # returns c the encrypted message
    return m ** e % n


def decrypt(c, d, n):
    # returns m the decrypted message
    return c ** d % n


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


if __name__ == "__main__":
    public_key_files = ["data/"+f for f in listdir("data/") if "pem" in f]
    print(public_key_files)

    for i in range(len(public_key_files)):

        pem1 = open(public_key_files[i]).read()
        k1 = RSA.importKey(pem1)
        n1 = k1.n
        e1 = k1.e
        flag = False
        for j in range(len(public_key_files)):
            if i != j:
                pem2 = open(public_key_files[j]).read()
                k2 = RSA.importKey(pem2)
                n2 = k2.n
                e2 = k2.e

                p = math.gcd(n1, n2)
                # print(p)
                if p != 1:
                    q = n1 // p
                    phi = (p - 1) * (q - 1)
                    d = modinv(e1, phi)
                    if d is not None:
                        # print(d)

                        dP = d % p
                        dQ = d % q
                        qInv = pow(q, p - 2, p)
                        key = pempriv(n1, e1, d, p, q, dP, dQ, qInv)
                        # print(key)

                        output_file_name = "data/key" + public_key_files[i].split("/")[1].split(".")[0] + ".pem"
                        f = open(output_file_name, "w")
                        f.write(key)
                        f.close()
                        flag = True
                        break
