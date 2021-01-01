from flask import Flask,render_template,redirect,url_for
from forms import XorEncryptionForm,VignereEncrpytionForm,CeasarEncrpytion
from encrpytion import cipherText, generateKey, xoren,encrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/?Xor??", methods=['GET', 'POST'])
def xor():
    form = XorEncryptionForm()
    if form.validate_on_submit():
        xor = xoren(form.plaintext.data)
        return render_template("xor.html",form = form,results = xor)
    return render_template("xor.html",form = form,results = None)

@app.route("/?Vignere??", methods=['GET', 'POST'])
def Vignere():
    form = VignereEncrpytionForm()
    if form.validate_on_submit():
        vignere = cipherText(form.plaintext.data , generateKey(form.plaintext.data,form.key.data))
        return render_template("vignere.html",form=form,results=vignere)
    return render_template("vignere.html",form=form,results=None)

@app.route("/?Ceasar??", methods=['GET', 'POST'])
def Ceasar():
    form = CeasarEncrpytion()
    if form.validate_on_submit():
        cesar = encrypt(form.plaintext.data,form.key.data)
        return render_template("ceasar.html",form = form,results=cesar)
    return render_template("ceasar.html",form = form,results=None)


if __name__ == '__main__':
    app.run(debug=True)