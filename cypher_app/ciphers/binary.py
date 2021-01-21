class Binary:
	"""Represents text to be ciphered into Binary and vice versa.

	Attributes:
		text (str): Text to cipher/decipher.
	"""


	def __init__(self, text):
		"""Initializes Binary class attributes."""
		self.text = text


	def cipher(self):
		"""Ciphers a string to Binary.

		Args:
		    None

		Returns:
		    str: Text ciphered into Binary
		"""
		return ' '.join(format(ord(char), 'b') for char in self.text)


	def decipher(self):
		"""Deciphers a string composed of binary values into ASCII text.

		Adapted from kite.com's "How to convert binary to string in Python:" (
		https://www.kite.com/python/answers/how-to-convert-binary-to-string-in
		-python).

		Args: 
			None

		Returns:
			str: Text deciphered from Binary to ASCII text.
		"""
		return ''.join(
			[chr(int(binary, 2)) for binary in binary_string.split(" ")])
