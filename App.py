from flask import Flask,render_template,jsonify

app = Flask(__name__)

users = [
    {
    "name":"Shreya",
    "Age":23
},
  {
    "name":"Priya",
    "Age":21
},
  {
    "name":"samiksha",
    "Age":22
}
]

@app.route("/")
def home():
    return render_template('Homepage.html',users=users)

@app.route("/api/jobs")
def Jobs():
    return jsonify(users)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
