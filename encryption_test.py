import unittest
import encryption
import sympy


class EncryptionUnitTests(unittest.TestCase):
    def test_prime_generator(self):
        primes = encryption.prime_generator()
        for prime in primes:
            self.assertTrue(sympy.isprime(prime))

    def test_mod_m_generator(self):
        eds = encryption.mod_m_generator(3, max_ed=10)
        self.assertEqual(eds, [4, 10])
        eds = encryption.mod_m_generator(2, max_ed=20)
        self.assertEqual(eds, [9, 15])
        eds = encryption.mod_m_generator(25, max_ed=300)
        self.assertEqual(eds, [26, 51, 76, 126, 176, 201, 226, 276])

    def test_ed_factorization(self):
        factors = encryption.ed_factorization(10)
        self.assertEqual(factors, [2, 5])
        factors = encryption.ed_factorization(36)
        self.assertEqual(factors, [2, 3, 4, 6, 9, 12, 18])
        factors = encryption.ed_factorization(12)
        self.assertEqual(factors, [2, 3, 4, 6])

    def test_is_prime(self):
        self.assertTrue(encryption.is_prime(13))
        self.assertTrue(encryption.is_prime(5))
        self.assertTrue(encryption.is_prime(61))
        self.assertTrue(encryption.is_prime(1223))
        self.assertFalse(encryption.is_prime(12))
        self.assertFalse(encryption.is_prime(2000))
        self.assertFalse(encryption.is_prime(1387))
        self.assertFalse(encryption.is_prime(1891))
        self.assertTrue(encryption.is_prime(2))

    def test_encryption(self):
        n, e, d = encryption.generate_rsa_keys()
        print(n, e, d)
        message = "hello"
        encrypted = encryption.encrypt(message, n, e)
        print(encrypted)
        decrypted = encryption.decrypt(encrypted, n, d)
        print(decrypted)


if __name__ == '__main__':
    unittest.main()
