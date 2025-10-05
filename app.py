from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

scores = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    score = data.get('score', 0)
    scores.append(score)
    return jsonify({'message': 'Score received!', 'scores': scores})

if __name__ == '__main__':
    app.run(debug=True)