import re


class PigLatin:
    """Represents text to be ciphered into Pig Latin.

    Attributes:
        text (str): Text to be ciphered into Pig Latin.
        vowels (str): Uppercase and lowercase vowels. Defined in __init__.
    """


    def __init__(self, text):
        """Initializes attributes of PigLatin."""
        self.text = text
        self.vowels = 'aeiouAEIOU'


    def _cipher_word(self, word):
        """Ciphers a word into Pig Latin. 

        Meant for use only within class in its translate() method.
        
        Args:
            word (str): Word to be ciphered into Pig Latin.

        Returns:
            str: Word ciphered into Pig Latin.
        """
        if word[0] in self.vowels or not any(c in word for c in self.vowels):
            return word + "yay"
        else:
            first_vowel = re.search(r'[aeiouAEIOU]', word).group()
            first_consonants = re.search(r'[^aeiouAEIOU]{1,}', word).group()
            return word[word.find(first_vowel):] + first_consonants + "ay"


    def cipher(self):
        """Ciphers self.text into Pig Latin.

        Args:
            None

        Returns:
            str: Text ciphered into Pig Latin
        """
        cipher = ""
        partitions = re.compile(r"[\w']+|[.,!?;]|\s").findall(self.text)
        for partition in partitions:
            # Only translate partition if made of alphabetical characters.
            if partition.isalpha():
                cipher += self._cipher_word(partition)
            else:
                cipher += partition
        return cipher