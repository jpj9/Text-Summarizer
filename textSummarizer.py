import nltk
import re

#converting para into list of sentences


class Summarizer:
    def __init__(self,text):
        self.text = text

    def getSummary(self):
        # converting para into list of sentences
        sent_text = nltk.sent_tokenize(self.text)

        # Removing Square Brackets and Extra Spaces
        remove_syn = lambda x: re.sub('[^a-zA-Z]', ' ', x)
        remove_dig = lambda x: re.sub(r'\s+', ' ', x)

        sent_text = list(map(remove_dig, (list(map(remove_syn, sent_text)))))

        stopwords = nltk.corpus.stopwords.words('english')

        def getWordDict(text):
            word_frequencies = {}
            for t in text:
                for word in nltk.word_tokenize(t):
                    if word not in stopwords:
                        if word not in word_frequencies.keys():
                            word_frequencies[word] = 1
                        else:
                            word_frequencies[word] += 1
            return word_frequencies

        word_freq_dict = getWordDict(sent_text)

        # finding weighed frequencies
        maximum_frequncy = max(word_freq_dict.values())  # max frequncy

        for word in word_freq_dict.keys():
            word_freq_dict[word] = (word_freq_dict[word] / maximum_frequncy)

        # Calculating Sentence Scores
        sentence_scores = {}
        for sent in sent_text:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_freq_dict.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_freq_dict[word]
                        else:
                            sentence_scores[sent] += word_freq_dict[word]

        import heapq
        summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

        summary = '.'.join(summary_sentences)
        return (summary)


