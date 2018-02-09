import random

def generate_random_text(num_chars): # returns a variable with random txt of length num_chars
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text


def mean(counts): # gets the mean of a list that has to do with unicode stuff
    total = 0
    for c in counts:
        character = chr(c)
        total += ord(character)

    avg = total / len(counts)        
        
    return avg

def chi_square(counts): # calculates chi square with unicode stuff
    expected = mean(counts)
    
    X = 0

    for n in counts:
        character = chr(n)
        observed = ord(character)
        top = observed - expected
        X += (top)**2

    return X/expected

def count_characters(text, counts): # counts the characters
    for c in text:
        n = ord(c)
        counts[n] += 1

content = generate_random_text(15000)

# code here to write content to a file

with open("random_text.txt", "w+") as f:
    f.write(content)

counts = [0] * 127
count_characters(content, counts)
print(counts)
print(chi_square(counts))

content = generate_random_text(5000)
content += 
# code here to write content to a file

with open("random_text.txt", "w+") as f:
    f.write(content)

counts = [0] * 127
count_characters(content, counts)
print(counts)
print(chi_square(counts))
