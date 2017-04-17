1. private-from-pq.c
Usage: private-from-pq p q
Output: A RSA private key file (in PEM format) containing p, q, d (on screen)

2. another_fac.c
Usage: another_fac n p
Output: Another factor for n if p is one factor.

3. gcd.c
Usage: gcd n1 n2
Output: gcd(n1, n2)

Compile: 
- gcc -I/openssl -o output_exe_file private-from-pq.c -lcrypto
(assume /openssl is the directory for openSSL library)