from Crypto.PublicKey import RSA
import math
import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64

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
    pem1 = open("../RSA Challenge (trial)/public2.pem").read()
    k1 = RSA.importKey(pem1)
    n1 = k1.n
    e1 = k1.e

    pem2 = open("../RSA Challenge (trial)/public3.pem").read()
    k2 = RSA.importKey(pem2)
    n2 = k2.n
    e2 = k2.e

    print("n1: ", n1)
    print("e1: ", e1)
    print("n2: ", n2)
    print("e2: ", e2)

    p = math.gcd(n1, n2)
    q = n2 // p
    phi = (p - 1) * (q - 1)
    d = modinv(e1, phi)
    print(d)
    print(hex(d))

    dP = d % p
    dQ = d % q
    qInv = pow(q, p - 2, p)
    key = pempriv(n2, e1, d, p, q, dP, dQ, qInv)
    print(key)
    f = open("../RSA Challenge (trial)/key3.pem", "w")
    f.write(key)
    f.close()