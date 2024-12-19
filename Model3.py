import spacy
from collections import Counter

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

class TextSummarization():
    def __init__(self):
        pass

    def summarize_text(self, text, n_sentences=3):
        """
        Summarizes the input text by extracting the most important sentences.
        
        Parameters:
        text (str): The input text to be summarized.
        n_sentences (int): The number of sentences to include in the summary.
        
        Returns:
        str: The summarized text.
        """
        doc = nlp(text)

        # Extract sentences and their importance scores
        sentences = [sent for sent in doc.sents]
        word_frequencies = Counter(token.text.lower() for token in doc if not token.is_stop and not token.is_punct)
        sentence_scores = {sent: sum(word_frequencies[token.text.lower()] for token in sent if token.text.lower() in word_frequencies) for sent in sentences}

        # Sort sentences by score and select the top n_sentences
        important_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:n_sentences]
        summary = ' '.join([sent.text for sent in important_sentences])
        
        return summary

if __name__ == "__main__":
    obj = TextSummarization()
    message = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. 
    Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize 
    its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) 
    that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving". As machines become increasingly 
    capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. A quip in 
    Tesler's Theorem says "AI is whatever hasn't been done yet."
"""
    print(obj.summarize_text(message))

