
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_no = ord(char)
    char_no = char_no + 1
    
    new_char = chr(char_no)
    encrypted_text = encrypted_text + new_char


print(plain_text)
print(encrypted_text)