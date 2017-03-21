from flask import Flask, url_for, render_template
from jinja2 import Markup

# flask potrebuje vzdy to app
# premenna nastavena pythonom na meno aktualneho modulu
app = Flask(__name__)

# print(__name__)

# FLASK DEBUG je super, ked robim na svojom pocitaci a skusam
# adresa, na ktorej tato stranka bude


@app.route('/')
def hello():
    # pomocou tohto mi vypise URL s tymito argumentami
    return url_for('hello_english', username='Daniel', count=3)

# mozem tam mat int, float, string, path (retazec, v ktorom nebudu lomitka)
# keby som chcel napriklad username, mozem do tam dat cez path


@app.route('/hello/')
@app.route('/hello/<username>/')
@app.route('/hello/<username>/<int:count>/')
def hello_english(username=None, count=1):
    return render_template('hello.html', name=username)
    # return 'Hello {}!'.format(username) * count


@app.template_filter('em')
def em(text):
    # pomocou markup oznacim, ze je to html, ktore je v poriadku
    return Markup('<em>{}</em>').format(text)
