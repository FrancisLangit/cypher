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

		Adapted from geeksforgeeks.org's "Python | Convert String to Binary" f
		-rom (https://www.geeksforgeeks.org/python-convert-string-to-binary/).

		Args:
		    None

		Returns:
		    tuple: ([int] 0, [str] Ciphered Text) 
		"""
		return (0, ' '.join(format(ord(char), 'b') for char in self.text))


	def decipher(self):
		"""Deciphers a string composed of binary values into ASCII text.

		Adapted from kite.com's "How to convert binary to string in Python" f-
		rom (https://www.kite.com/python/answers/how-to-convert-binary-to-stri
		ng-in-python).

		Args: 
			None

		Returns:
			tuple: ([int] Error Code, [str] Output Text) 
				[int] Error Code - 0 if with error. 1 without error.
				[str] Output Text - Deciphered text or error message.
		"""
		try:
			return (0, ''.join(
				[chr(int(binary, 2)) for binary in self.text.split(" ")]))
		except ValueError:
			return (1, 'Error. Could not decipher input into binary.')