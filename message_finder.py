def mean(counts): # gets the mean of a list that has to do with unicode stuff
    total = 0
    for c in counts:
        total += c

    avg = total / len(counts)        
        
    return avg

def chi_square(counts): # calculates chi square with unicode stuff
    expected = mean(counts)
    
    X = 0

    for observed in counts:
        top = observed - expected
        X += (top)**2

    return X/expected

def count_characters(text): # counts the characters
    counts = [0] * 127
    for c in text:
        n = ord(c)
        counts[n] += 1

    return counts[32:]

def get_filename(num):
    zeros = ""
    if num < 10:
        zeros = "00000"
    elif num < 100:
        zeros= "0000"
    elif num < 1000:
        zeros = "000"
    elif num < 10000:
        zeros = "00"
    elif num < 100000:
        zeros = "0"
    return "file_" + zeros + str(num) + ".txt"


for i in range(0, 17999):
    filename = get_filename(i)
    with open("text_files/" + filename, 'r') as f:
        contents = f.read()
    counts = count_characters(contents)
    chi_value = chi_square(counts)
#    with open("chi_values.txt", 'a') as c:
#        c.write(filename + " " + str(chi_value) + "\n")
    if chi_value < 55 or chi_value > 140:
        print(filename, chi_value)



print("Done looping.")
