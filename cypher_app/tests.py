from django.test import TestCase
from cypher_app.ciphers import (
	binary,
	caesar_cipher,
	morse_code,
	pig_latin,
)


class CiphersTestCase(TestCase):


	def setUp(self):
		self.cipher_text = "The quick brown fox jumps over the lazy dog."

		self.cipher_binary = binary.Binary(self.cipher_text)
		self.cipher_caesar = caesar_cipher.CaesarCipher(self.cipher_text, 2)
		self.cipher_morse = morse_code.MorseCode(self.cipher_text)
		self.cipher_pig = pig_latin.PigLatin(self.cipher_text)


	def test_cipher(self):
		self.assertEqual(self.cipher_morse.cipher(),
			"- .... . ....... --.- ..- .. -.-. -.- ....... -... .-. --- .-- -." + 
			"....... ..-. --- -..- ....... .--- ..- -- .--. ... ....... --- ..." +
			"- . .-. ....... - .... . ....... .-.. .- --.. -.-- ....... -.. ---" +
			" --. .-.-.-"
			)
		self.assertEqual(self.cipher_caesar.cipher(),  
			"Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.")
