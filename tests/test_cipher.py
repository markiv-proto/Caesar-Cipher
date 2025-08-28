import unittest
from caesar.cipher import caesar_encrypt, caesar_decrypt, caesar_bruteforce

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        # Uppercase input
        self.assertEqual(caesar_encrypt("SOFTWARE", 3), "VRIWZDUH")
        # Lowercase input
        self.assertEqual(caesar_encrypt("software", 3), "vriwzduh")
        # Mixed case input
        self.assertEqual(caesar_encrypt("Software", 3), "Vriwzduh")
        # Non-alphabet characters
        self.assertEqual(caesar_encrypt("Soft 123!", 3), "Vriw 123!")

    def test_decrypt(self):
        self.assertEqual(caesar_decrypt("VRIWZDUH", 3), "SOFTWARE")
        self.assertEqual(caesar_decrypt("vriwzduh", 3), "software")
        self.assertEqual(caesar_decrypt("Vriwzduh", 3), "Software")
        self.assertEqual(caesar_decrypt("Vriw 123!", 3), "Soft 123!")

    def test_bruteforce(self):
        encrypted = caesar_encrypt("Software", 3)
        results = caesar_bruteforce(encrypted)
        # Ensure correct decryption is in results
        self.assertIn("Software", results.values())
        # Ensure dictionary has 25 possible shifts
        self.assertEqual(len(results), 25)
        # Ensure shift=3 gives us back the original
        self.assertEqual(results[3], "Software")


if __name__ == "__main__":
    unittest.main()
