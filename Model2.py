from textblob import TextBlob

class Sentimentanalysis:
    def __init__(self):
        pass
    
    def sentiment_analysis(self,sentence): 
        polarity = TextBlob(sentence).sentiment.polarity
        if polarity > 0: 
            return "It is a positive sentiment." 
        elif polarity < 0: 
            return "It is a negative sentiment." 
        else: 
            return "The sentiment is triky to understand. I'll call it a neutral sentiment."
        
if __name__  == "__main__":

    obj2 = Sentimentanalysis()
    message = "I cannot believe I enjoyed this as much as I did. The anthology stories were better than par, but the linking story and its surprise ending hooked me. Alot of familiar faces will keep you asking yourself 'where I have I seen them before?'' Forget the running time listed on New Line\'s tape, this ain\'t no 103 minutes, according to my VCR timer and IMDB. Space Maggot douses the campfire in his own special way and hikes this an 8."
    print(obj2.sentiment_analysis(message))