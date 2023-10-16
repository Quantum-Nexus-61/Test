import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Input text - to summarize
text = """The quality, type, and density of information conveyed via text varies from source to source. Textbooks tend to be low in density but high in quality, while academic articles are high in both quality and density. On the other hand, news articles can vary significantly from source to source. Regardless of where the text comes from the goal here is to minimize the time you spend reading. Thus, we will build a tool that can easily be adapted to any number of sources."""

# Process the text with spaCy
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
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

print(summary)
