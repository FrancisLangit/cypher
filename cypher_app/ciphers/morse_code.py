class MorseCode:
     """Represents text to be ciphered into Morse Code.

     Attributes:
          text (str): Text to be ciphered into morse code.
          morse_code_dict (dict): Dictionary of morse code equivalents.
     """


     def __init__(self, text):
          """Initializes MorseCode class attributes."""
          self.text = text
          self.morse_code_dict = { 
               # Letters
               'A': '.-'    ,      'B': '-...'   ,      'C': '-.-.'  , 
               'D': '-..'   ,      'E': '.'      ,      'F': '..-.'  , 
               'G': '--.'   ,      'H': '....'   ,      'I': '..'    , 
               'J': '.---'  ,      'K': '-.-'    ,      'L': '.-..'  , 
               'M': '--'    ,      'N': '-.'     ,      'O': '---'   , 
               'P': '.--.'  ,      'Q': '--.-'   ,      'R': '.-.'   , 
               'S': '...'   ,      'T': '-'      ,      'U': '..-'   , 
               'V': '...-'  ,      'W': '.--'    ,      'X': '-..-'  , 
               'Y': '-.--'  ,      'Z': '--..'   , 

               # Digits
               '1': '.----' ,      '2': '..---'  ,      '3': '...--' , 
               '4': '....-' ,      '5': '.....'  ,      '6': '-....' , 
               '7': '--...' ,      '8': '---..'  ,      '9': '----.' , 
               '0': '-----' , 

               # Punctuation Marks
               '.': '.-.-.-',      ',': '--..--' ,      '?': '..--..',
               "'": '.----.',      '!': '-.-.--' ,      '/': '-..-.' ,
               "(": '-.--.' ,      ')': '-.--.-' ,      '&': '.-...' ,
               ":": '---...',      ';': '-.-.-.' ,      '=': '-...-' ,
               '+': '.-.-.' ,      '-': '-....-' ,      '_': '..--.-',
               '"': '.-..-.',      '$': '...-..-',      '@': '.--.-.' 
          } 


     def cipher(self): 
          """Ciphers a string into morse code.

          Args:
              None

          Returns:
              str: Text ciphered into Morse Code
          """
          try:
               cipher = '' 
               for char in self.text.upper(): 
                    if char != ' ': 
                         cipher += self.morse_code_dict[char] + ' '
                    else: 
                         cipher += ' '
          except KeyError as e:
               return f'Error. Cannot translate {e} to morse code.'
          return cipher