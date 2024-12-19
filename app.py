from flask import Flask, request,render_template
from Model import SpellCheckerModule
from Model2 import Sentimentanalysis
from Model3 import TextSummarization

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()
sentiment_analysis_module = Sentimentanalysis()
text_summarization_module = TextSummarization()

# routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main')
def index():
    return render_template('index.html')

@app.route('/summarization')
def sumarization():
    return render_template('summarization.html')

@app.route('/sentiment')
def sentimentss():
    return render_template('sentiment.html')



# -----------------------------------------------For Spell Checker----------------------------------------
@app.route('/spell',methods=['POST','GET'])
def spell():
    if request.method=='POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        corrected_grammar = spell_checker_module.correct_grammar(text)
        return render_template('index.html',corrected_text=corrected_text,corrected_grammar=corrected_grammar, text = text)

@app.route('/grammar',methods=['POST','GET'])
def grammar():
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        corrected_file_grammar = spell_checker_module.correct_grammar(readable_file)
    return render_template('index.html',corrected_file_text=corrected_file_text,corrected_file_grammar=corrected_file_grammar, readable_file = readable_file)

#------------------------------------------------------------------------------------------------------------

#--------------------------------------------for Sentiment analysis------------------------------------------
@app.route('/senti',methods=['POST','GET'])
def sentiment():
    sentimented_analysis = None
    correct_text = None
    if request.method == 'POST':
        text = request.form['text']
        correct_text = spell_checker_module.correct_grammar(text)
        sentimented_analysis = sentiment_analysis_module.sentiment_analysis(correct_text)
    return render_template('sentiment.html', sentimented_analysis = sentimented_analysis, correct_text = correct_text)

@app.route('/sentimented',methods=['POST','GET'])
def sentiment_file():
    sentimented_analysis = None
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        corrected_text_file = spell_checker_module.correct_grammar(readable_file)
        sentimented_analysis_file = sentiment_analysis_module.sentiment_analysis(corrected_text_file)
    return render_template('sentiment.html', sentimented_analysis_file = sentimented_analysis_file, corrected_text_file = corrected_text_file)

#------------------------------------------------------------------------------------------------------

#------------------------------------------for text summarization--------------------------------------

@app.route('/summarize',methods=['POST','GET'])
def text_summarization():
    text_summarize = None
    if request.method == 'POST':
        text = request.form['text']
        text_summarize = text_summarization_module.summarize_text(text)
    return render_template('summarization.html', text_summarize = text_summarize, text = text )

@app.route('/summarized',methods=['POST','GET'])
def text_summarization_file():
    text_summarize = None
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        text_summarize_file = text_summarization_module.summarize_text(readable_file)
    return render_template('summarization.html', text_summarize_file = text_summarize_file, readable_file = readable_file)






# python main
if __name__ == "__main__":
    app.run(debug=True)