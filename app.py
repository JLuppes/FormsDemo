from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import validators, ColorField, StringField, IntegerField, BooleanField, EmailField, RadioField
from wtforms.widgets.core import EmailInput

app = Flask(__name__)

app.secret_key = 'top-secret'


@app.route('/')
def index():
    return redirect(url_for('profile'))


class ProfileForm(FlaskForm):
    name = StringField('Name', [
        validators.InputRequired(message="Please enter your name!")
    ])
    email = EmailField('Email', [
        validators.Email(message="That\'s not a valid email!")
    ], widget=EmailInput())
    quan = IntegerField('Number of Guests', [
        validators.NumberRange(
            min=1, max=10, message="Please choose between 1 and 10!")
    ])
    comments = StringField('Comments', [
        validators.Length(
            min=0, max=100, message="Please keep your comments brief!")
    ])
    rel = RadioField('Relationship',
                     choices=[
                         "first",
                         "second"
                     ])
    accommodations = BooleanField('Accommodations', [
        validators.AnyOf(
            [True, False], message="Do you need accommodations?")
    ])
    faveColor = ColorField("Favorite Color")


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():

        return render_template(
            'profileSuccess.html',
            form=form
        )

    return render_template('profileForm.html', form=form)
