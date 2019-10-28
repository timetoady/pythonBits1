plain_text = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plain_text:
    ordvalue = ord(ch)
    cipher_value = ordvalue + distance
    if cipher_value > ord('~'):
        cipher_value = ord(' ') + distance - 1
    code += chr(cipher_value)
print(code)