from textblob import TextBlob
from pyaspeller import YandexSpeller


class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        
    def correct_spell(self,text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)
    
    def correct_grammar(self,text):
        speller = YandexSpeller()
        fixed = speller.spelled(text)
        return fixed 
    


if __name__  == "__main__":
    obj = SpellCheckerModule()

    message = "I cannot believe I enjoyed this as much as I did. The anthology stories were better than par, but the linking story and its surprise ending hooked me. Alot of familiar faces will keep you asking yourself 'where I have I seen them before?'' Forget the running time listed on New Line\'s tape, this ain\'t no 103 minutes, according to my VCR timer and IMDB. Space Maggot douses the campfire in his own special way and hikes this an 8."
    print(obj.correct_spell(message))
    print(obj.correct_grammar(message))
