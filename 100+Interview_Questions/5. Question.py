# 4. counting CONSONANTS in a given word
# volwel = ['a', 'e', 'i', 'o', 'u']
# word = "programming"

vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for char in word:
    if char not in vowel: # here jus t you have to add (not in)
        count += 1
print(count)
