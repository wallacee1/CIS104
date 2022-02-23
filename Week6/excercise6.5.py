text = "X-DSPAM-Confidence:0.8475"

word = text.find(':')
fword = text[word+2:]

value = float(fword)

print(value)