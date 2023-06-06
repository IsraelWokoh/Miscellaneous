from secrets import randbelow

def sponge(text):
	new = ''
	for char in text:
		new += char.upper() if randbelow(2) else char.lower()
	return new

while True:
	print(
		sponge(
			input(f'\n{sponge("Enter text to rANdOmiSe: ")}')
		)
	)
