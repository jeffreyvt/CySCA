#include <stdlib.h>
#include <openssl/bn.h>
#include <openssl/engine.h>



int
main (int argc, char *argv[])
{

  BIGNUM *p = BN_new ();
  BIGNUM *q = BN_new ();
  BIGNUM *tmp = BN_new ();
  BIGNUM *ZERO = BN_new ();
  BN_CTX *ctx = BN_CTX_new ();
    
  char *result;

  if (argc < 3)
    {
      fprintf (stderr, "usage: %s n1 n2\n", argv[0]);
      exit (1);
    }

  if (!(BN_dec2bn (&p, argv[1])) || !(BN_dec2bn (&q, argv[2]))) {
      fprintf (stderr, "usage: %s n1 n2\n", argv[0]);
      exit (1);
  }
  
  // set ZERO = 0
  BN_zero(ZERO);

  if (BN_cmp(p, q) == -1)
	  BN_swap(p,q);
  
  // Now p > q
  
  while( BN_cmp(q, ZERO) != 0)
  {
	  /* tmp = p mod q */
		BN_mod (tmp, p, q, ctx);
		p = BN_copy(p,q);
	    q = BN_copy(q,tmp);
  }
  
  result = BN_bn2dec(p);
  
  printf("GCD is: %s ", result);
  
    /* Release allocated objects */
  BN_CTX_free (ctx);
  BN_clear_free (tmp);
  BN_clear_free (p);
  BN_clear_free (q);
  BN_clear_free (ZERO);

}
