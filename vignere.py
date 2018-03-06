def vig_decrypt(ciphertext, key):
    k_len = len(key)
    k_int = []
    for i in key:
        k_int.append(ord(i))
    c_int = []
    for j in ciphertext:
        c_int.append(ord(j))

    return_text = ""

    for i in range(len(c_int)):
        num = k_int[i%k_len]
        num2 = (c_int[i] - 32 - num) % 95
        return_text += chr(num2 + 32)

    return return_text

with open("text_files/file_012499.txt", 'r') as f:
    contents = f.read()

text= vig_decrypt(contents, "enigma")

print(text)
