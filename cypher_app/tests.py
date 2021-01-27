from django.test import TestCase
from cypher_app.ciphers import (
	binary,
	caesar_cipher,
	morse_code,
	pig_latin,
)


class CiphersTestCase(TestCase):
	"""Test case for ciphering and deciphering algorithms."""


	def setUp(self):
		"""Method to prepare class attributes."""
		self.short_text = "Slim!"
		self.long_text = "The quick brown fox jumps over the lazy dog."
		self.caesar_key = 2

		self.cipher_binary = binary.Binary(self.short_text)
		self.cipher_caesar = caesar_cipher.CaesarCipher(
			self.long_text, self.caesar_key)
		self.cipher_morse = morse_code.MorseCode(self.short_text)
		self.cipher_pig = pig_latin.PigLatin(self.long_text)


	def test_cipher(self):
		"""Evaluates ciphering algorithms."""
		self.assertEqual(self.cipher_binary.cipher(),
			"1010011 1101100 1101001 1101101 100001")
		self.assertEqual(self.cipher_caesar.cipher(),  
			"Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.")
		self.assertEqual(self.cipher_morse.cipher(), 
			"... .-.. .. -- -.-.-- ")
		self.assertEqual(self.cipher_pig.cipher(), 
			"heTay uickqay rownbay oxfay umpsjay overyay hetay azylay ogday.")


	def test_decipher(self):
		"""Evaluates deciphering algorithms."""
		self.assertEqual(
			binary.Binary(
				"1010011 1101100 1101001 1101101 100001").decipher(), 
			self.short_text
		)
		self.assertEqual(
			caesar_cipher.CaesarCipher(
				"Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.", 
				self.caesar_key).decipher(), 
			self.long_text
		)
		self.assertEqual(
			morse_code.MorseCode("... .-.. .. -- -.-.-- ").decipher(),
			self.short_text.upper(),
		)
		self.assertEqual(
			pig_latin.PigLatin((
				"heTay uickqay rownbay oxfay umpsjay overyay hetay"
				" azylay ogday.")).decipher(),
			self.long_text,
		)