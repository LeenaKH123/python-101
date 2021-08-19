# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"
print("german word length", len(longest_german_word))
print("hungarian word length", len(longest_hungarian_word))
print("finish word length", len(longest_finnish_word))
print("strong password length", len(strong_password))
test_list = [
    longest_german_word,
    longest_hungarian_word,
    longest_finnish_word,
    strong_password,
]
# max_length = -1
counter = 0
result = ""
for char in test_list:
    counter += 1
    if test_list[counter] > test_list[counter + 1]:
        result = test_list[counter]
        counter += 1

print(result)
print(
    "the length of the longest string is",
    max(
        len(longest_german_word),
        len(longest_hungarian_word),
        len(longest_finnish_word),
        len(strong_password),
    ),
)
