word = "     She is a nice lady"
print(word)

adjusted = word.lstrip()
print(adjusted)

word2 = "She is a nice lady                      "
word3 = word2.rstrip()
print("word3: ", word3)
print("word2: ", word2)
more_data = "Isn't she?"

# I am trying to combine two variables using formatting
# New way of formatting from Python version 3.6 and above
new_word = f"{word2}{more_data}"
print(new_word)

# Old way of formatting from Python version 3.5 and below
new_word_2 = "{}{}".format(word2, more_data)
print(new_word_2)


fresh_word = "              He is happy!                 "
print(fresh_word)
fresh_word = fresh_word.strip()
print(fresh_word)


 