class Binary:
	"""Represents text to be ciphered into Binary.

	Attributes:
		text (str): Text to cipher.
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