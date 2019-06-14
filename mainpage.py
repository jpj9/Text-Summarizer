from flask import Flask, jsonify, request, abort, json,render_template,url_for

from forms import InputForm,OutputForm

from  textSummarizer import Summarizer

secret_key = '2f2d5287db25aed'


test_dict = [
    {
        'name':'jay',
        'hometown':'sikar',
    },
    {
        'name': 'shiv',
        'hometown': 'alwar',
    },

]

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key

# @app.route("/")
# def root():
#     return render_template('home.html',data = test_dict, title = 'HomePage')


#this section will have info about the textsum
@app.route("/about")
def about():
    return render_template('about.html', title='About Page')


#actual app goes here
@app.route("/")
@app.route("/apptext",methods=['GET','POST'])
def appText():
    form = InputForm()
    input_text = form.textInput._value()
    # print(input_text)
    # sum1 = Summarizer(input_text)
    #
    # summary = sum1.getSummary()
    if(input_text):
        sum1 = Summarizer(input_text)
        summary = sum1.getSummary()
        return render_template('app.html', form=form, output=summary, title='App page')
    else:
        return render_template('app.html', form=form, output='type something', title='App page')








if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=6001)


