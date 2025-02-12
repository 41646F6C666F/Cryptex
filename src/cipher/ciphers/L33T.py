"""
Author: @marvhus
"""
from cipher import Cipher

class L33T(Cipher): #make sure you change this from text to your cipher

    name = 'L33t Sp34k' #change the name
    type = 'cipher'

    leet_speak = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '9',
        'i': '1',
        's': '5',
        't': '7',
        'z': '2',
    }
    inverse_leet_speak = dict((v, k) for k,v in leet_speak.items())

    convertWithDict = lambda dict, char : dict[char] if char in dict else char     

    @staticmethod
    def encode(args):
        text = args.text.lower()

        if not text:
            return {'text': "No input text", 'success': False}

        output = ''.join(L33T.convertWithDict(L33T.leet_speak, char) for char in text)

        return {'text': output, 'success': True}

    @staticmethod
    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = ''.join(L33T.convertWithDict(L33T.inverse_leet_speak, char) for char in text)

        return {'text': output, 'success': True}

    @staticmethod
    def print_options():
        #Edit this section as needed for your specific encoding / decoding.
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py l33t -e -t 'hello'
        python main.py l33t -d -t 'h3llo'
        ''')
