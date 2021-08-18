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
print(
    "the longest string is",
    max(
        longest_german_word,
        longest_hungarian_word,
        longest_finnish_word,
        strong_password,
    ),
    max(
        len(longest_german_word),
        len(longest_hungarian_word),
        len(longest_finnish_word),
        len(strong_password),
    ),
)
