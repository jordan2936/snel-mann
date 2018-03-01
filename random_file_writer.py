import random

def generate_random_text(num_chars): # returns a variable with random txt of length num_chars
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text

filenumber = random.randint(1,3000)
filename = "random_file_" + str(filenumber) + ".txt"

with open(filename, 'w+') as f:
    contents = generate_random_text(20000)
    f.write(contents)
