#Opening h.txt file.
file_contnets = open("h.txt","r")

result = {}
a = file_contents.split()
for word in a:
    if word in uninteresting_words:
        pass
    else:
        for letter in word:
            if letter in punctuations:
                letter.replace(punctuations, "")
        if word not in result.keys():
            result[word]=0
        else:
            result[word]+=1
