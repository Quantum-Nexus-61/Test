import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Input text - to summarize
text = """Japanese torpedo bombers flew just 50 feet above the water as they fired at the U.S. ships in the harbor, while other planes strafed the decks with bullets and dropped bombs."""

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
