string = 'Hello World'
direction = input('Left or right? (L/R) ').lower().strip()
shift = int(input('Shift by how much? '))
if direction == 'r':
    string = string[-shift:] + string
    string = string[:-shift]
else:
    string += string[:shift]
    string = string[shift:]
print(string)