from flask import Flask

app = Flask(__name__)


@app.route('/getmax/<a>/<b>')
def get_max(a, b):
    if a > b:
        return 'Max number is ' + a
    else:
        return 'Max number is ' + b


@app.route('/longestword/<word1>/<word2>/<word3>')
def get_longest_word(word1, word2, word3):
    if len(word1) > len(word2) and len(word1) > len(word3):
        return word1
    elif len(word2) > len(word1) and len(word2) > len(word3):
        return word2
    else:
        return word3


if __name__ == '__main__':
    app.run(debug=True)