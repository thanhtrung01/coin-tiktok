from flask import Flask, render_template

app = Flask(__name__)

@app.route('/coin')
def coin_page():
    return render_template('coin.html')

if __name__ == '__main__':
    app.run(port=5000)
