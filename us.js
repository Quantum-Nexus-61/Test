document.addEventListener("DOMContentLoaded", function () {
    const inputText = document.getElementById("inputtext");
    const summarizeButton = document.getElementById("summarizebutton");
    const summary = document.getElementById("summary");

    // Function to tokenize text and generate a summary
    function generateSummary(text) {
        const words = text.split(/\s+/);
        const sentences = text.split(/[.!?]/);

        // Create a frequency table to keep the score of each word
        const freqTable = {};

        words.forEach((word) => {
            word = word.toLowerCase();
            if (freqTable[word]) {
                freqTable[word]++;
            } else {
                freqTable[word] = 1;
            }
        });

        // Create a dictionary to keep the score of each sentence
        const sentenceValue = {};

        sentences.forEach((sentence) => {
            words.forEach((word) => {
                if (sentence.toLowerCase().includes(word)) {
                    if (sentenceValue[sentence]) {
                        sentenceValue[sentence] += freqTable[word];
                    } else {
                        sentenceValue[sentence] = freqTable[word];
                    }
                }
            });
        });

        // Calculate the average value of a sentence from the original text
        const values = Object.values(sentenceValue);
        const sumValues = values.reduce((sum, value) => sum + value, 0);
        const average = Math.floor(sumValues / values.length);

        // Store sentences into the summary
        let summary = '';
        sentences.forEach((sentence) => {
            if (sentenceValue[sentence] && sentenceValue[sentence] > 1.2 * average) {
                summary += ' ' + sentence;
            }
        });

        return summary;
    }

    summarizeButton.addEventListener("click", function () {
        const text = inputText.value;

        // Generate the summary using the function
        const summaryText = generateSummary(text);

        // Display the summary
        summary.textContent = summaryText;
    });
});
