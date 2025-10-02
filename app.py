from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = 'top-secret'


@app.route('/')
def index():
    return redirect(url_for('profile'))


class HistoryObject:
    def __init__(self, name, email, quan, comments, rel, accommodations):
        self.name = name
        self.email = email
        self.quan = quan
        self.comments = comments
        self.rel = rel
        self.accommodations = accommodations


historyList = list()


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        quan = request.form.get('quan', '').strip()
        comments = request.form.get('comments', '').strip()
        rel = request.form.get('rel', '').strip()
        accommodations = request.form.get(
            'accommodations') == "yes"  # True if checked

        # Validation
        if not name or not email or not quan or not rel:
            error = "Please fill in all required fields"
            return render_template('profileForm.html', error=error)

        historyList.append(HistoryObject(name, email, quan,
                                         comments, rel, accommodations))

        return render_template(
            'profileSuccess.html',
            name=name,
            email=email,
            quan=quan,
            comments=comments,
            rel=rel,
            accommodations=accommodations
        )

    return render_template('profileForm.html')


@app.route("/history")
def history():
    return render_template('history.html', history=list(historyList), len=len(historyList))
