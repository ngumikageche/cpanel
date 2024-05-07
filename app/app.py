from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classic')
def classic():
    return render_template('classic.html')

@app.route('/404')
def page_404():
    return render_template('404.html')

@app.route('/500')
def page_500():
    return render_template('500.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

@app.route('/boxed')
def boxed():
    return render_template('boxed.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/chartjs')
def chartjs():
    return render_template('chartjs.html')


@app.route('/collapsed-sidebar')
def collapsed_sidebar():
    return render_template('collapsed-sidebar.html')

@app.route('/compose')
def compose():
    return render_template('compose.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/editors')
def editors():
    return render_template('editors.html')

@app.route('/fixed')
def fixed():
    return render_template('fixed.html')

@app.route('/flot')
def flot():
    return render_template('flot.html')

@app.route('/general')
def general():
    return render_template('general.html')

@app.route('/icons')
def icons():
    return render_template('icons.html')

@app.route('/inline')
def inline():
    return render_template('inline.html')

@app.route('/invoice-print')
def invoice_print():
    return render_template('invoice-print.html')

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

@app.route('/lockscreen')
def lockscreen():
    return render_template('lockscreen.html')

@app.route('/mailbox')
def mailbox():
    return render_template('mailbox.html')

@app.route('/modals')
def modals():
    return render_template('modals.html')

@app.route('/morris')
def morris():
    return render_template('morris.html')

@app.route('/read-mail')
def read_mail():
    return render_template('read-mail.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/simple')
def simple():
    return render_template('simple.html')

@app.route('/sliders')
def sliders():
    return render_template('sliders.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/top-nav')
def top_nav():
    return render_template('top-nav.html')

@app.route('/widgets')
def widgets():
    return render_template('widgets.html')


if __name__ == '__main__':
    app.run(debug=True)