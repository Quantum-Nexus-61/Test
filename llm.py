import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Input text - to summarize
text = """The island nation of Japan, isolated from the rest of the world for much of its history, embarked on a period of aggressive expansion near the turn of the 20th century. Two successful wars, against China in 1894-95 and the Russo-Japanese War in 1904-05, fueled these ambitions, as did Japan’s successful participation in World War I (1914-18) alongside."""

doc = nlp(text)

# Tokenizing the text and generating sentences
words = [token.text for token in doc]
sentences = [sent.text for sent in doc.sents]

# Create a frequency table to keep the score of each word
freqTable = dict()
for word in words:
    word = word.lower()
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Create a dictionary to keep the score of each sentence
sentenceValue = dict()
for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

# Calculate the average value of a sentence from the original text
sumValues = sum(sentenceValue.values())
average = int(sumValues / len(sentenceValue))

# Store sentences into the summary
summary = ""
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

print(summary)
