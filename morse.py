class Solution:

	def run(self, morseToEnglish, textToTranslate):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#

		translatedText = ''
		if textToTranslate == '':
			return 'Invalid Morse Code Or Spacing'

		mTE_decode = {
			".-": "A",
			"-...": "B",
			# "-…": 'B',
			"-.-.": "C",
			"-..": "D",
			".": "E",
			"..-.": "F",
			"--.": "G",
			"....": "H",
			# "….": 'H',
			"..": "I",
			".---": "J",
			"-.-": "K",
			".-..": "L",
			"--": "M",
			"-.": "N",
			"---": "O",
			".--.": "P",
			"--.-": "Q",
			".-.": "R",
			"...": "S",
			# "…": 'S',
			"-": "T",
			"..-": "U",
			"...-": "V",
			# "…-": 'V',
			".--": "W",
			"-..-": "X",
			"-.--": "Y",
			"--..": "Z",
			".-.-.-": ".",
			"-----": "0",
			".----": "1",
			"..---": "2",
			"...--": "3",
			"....-": "4",
			".....": "5",
			"-....": "6",
			"--...": "7",
			"---..": "8",
			"----.": "9"
		}
		eTM_decode = {k:v for v,k in mTE_decode.items()}

		if morseToEnglish:
			for morseWord in textToTranslate.split('   '): # Split into words
				if morseWord != morseWord.strip(): # Invalid spacing
					return 'Invalid Morse Code Or Spacing'
				for morseLetter in morseWord.split():
					try:
						translatedText += f'{mTE_decode[morseLetter]}'
					except KeyError: # Invalid morse
						return 'Invalid Morse Code Or Spacing'
				translatedText += ' ' # Space between words

		else: # English to Morse
			for englishWord in textToTranslate.upper().split(): # Split words
				for englishLetter in englishWord:
					translatedText += f'{eTM_decode[englishLetter]} '
				translatedText += '  ' # Three spaces between words in Morse

		return translatedText.strip().lower()

# Solution.run(
# 	self,
# 	False,
# 	'UHFLOA V'
# )

# run(
# 	False,
# 	'The wizard quickly jinxed the gnomes before they vaporized.'
# )