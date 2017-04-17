#include <stdlib.h>
#include <openssl/bn.h>
#include <openssl/engine.h>



int
main (int argc, char *argv[])
{

  BIGNUM *n = BN_new ();
  BIGNUM *q = BN_new ();
  BIGNUM *p = BN_new ();
  BIGNUM *r = BN_new ();
  BIGNUM *ZERO = BN_new ();
  BN_CTX *ctx = BN_CTX_new ();
    
  char *result;

  if (argc < 3)
    {
      fprintf (stderr, "usage: %s n q\n", argv[0]);
      exit (1);
    }

  if (!(BN_dec2bn (&n, argv[1])) || !(BN_dec2bn (&q, argv[2]))) {
      fprintf (stderr, "usage: %s n q\n", argv[0]);
      exit (1);
  }
  
  // set ZERO = 0
  BN_zero(ZERO);
  
  if (BN_cmp(n, q) == -1)
	  BN_swap(n,q);
  
   
  // Now n > q
  
  BN_div(p, r, n, q, ctx); 
  result = BN_bn2dec(p);
  
  if (BN_cmp(r, ZERO) == 0)
	  // Remainder == 0 --> p is a factor of n
	  printf("Another factor is: %s ", result);
  else
	  printf("p is not a factor of n.");
  
    /* Release allocated objects */
  BN_CTX_free (ctx);
  BN_clear_free (n);
  BN_clear_free (p);
  BN_clear_free (q);
  

}
