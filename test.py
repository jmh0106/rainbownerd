EngSentence = "Hello You"
EngSentence = EngSentence.lower()
EngLetterList = list(EngSentence)
EmojiLetterList = []

for letter in EngLetterList:
    if letter != " ":
        EmojiLetterList.append(":regional_indicator_" + letter + ":")
    else:
        EmojiLetterList.append(" ")

print(''.join(EmojiLetterList))