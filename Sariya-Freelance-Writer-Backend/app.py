from flask import Flask, render_template, request, jsonify
from flask import Flask
from waitress import serve


app = Flask(__name__)

# Simulated database (in-memory storage for demo purposes)
writeups = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add_writeup', methods=['POST'])
def add_writeup():
    data = request.json
    new_writeup = {
        'id': len(writeups) + 1,
        'title': data['title'],
        'category': data['category'],
        'content': data['content']
    }
    writeups.append(new_writeup)
    return jsonify({'message': 'Write-up added successfully'})

@app.route('/get_writeups')
def get_writeups():
    return jsonify(writeups)

if __name__ == '__main__':
    app.run(debug=True)
    serve(app, host="0.0.0.0", port=8080)
