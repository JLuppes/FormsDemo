from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, BooleanField, EmailField, RadioField


app = Flask(__name__)

app.secret_key = 'top-secret'


@app.route('/')
def index():
    return redirect(url_for('profile'))


class ProfileForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired(
        message="Please enter your name!")])
    email = EmailField('email', [validators.Email(
        message="That\'s not a valid email!")])
    quan = IntegerField('quan', [validators.NumberRange(
        min=1, max=10, message="Please choose between 1 and 10!")])
    comments = StringField('comments', [validators.Length(
        min=0, max=100, message="Please keep your comments brief!")])
    rel = RadioField('rel', choices=["first", "second"])
    accommodations = BooleanField('Accommodations', [validators.AnyOf(
        [True, False], message="Do you need accommodations?")])


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():

        return render_template(
            'profileSuccess.html',
            form=form
        )

    return render_template('profileForm.html', form=form)
