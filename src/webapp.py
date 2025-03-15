from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTMLフォームのテンプレート
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>入力フォーム</title>
</head>
<body>
    <h2>入力フォーム</h2>
    <form action="/submit" method="post">
        <label for="name">名前:</label>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">メールアドレス:</label>
        <input type="email" id="email" name="email" required><br><br>
        <input type="submit" value="送信">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(form_html)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f"名前: {name}<br>メールアドレス: {email}"

if __name__ == '__main__':
    app.run(debug=True)

