from flask import Flask, request, render_template_string
import csv

app = Flask(__name__)

# Load CSV into a dictionary
seating = {}
with open('seating.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        seating[row['name'].lower()] = row['seat_number']

# HTML Template
form_html = """
<!doctype html>
<html lang="en">
<head>
  <title>Seat Lookup</title>
  <style>
    body {
      background: linear-gradient(to right, #6a11cb, #2575fc);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: white;
      text-align: center;
      padding-top: 100px;
    }

    h2 {
      font-size: 2em;
      margin-bottom: 30px;
    }

    form {
      background: rgba(255, 255, 255, 0.1);
      padding: 30px;
      border-radius: 15px;
      display: inline-block;
      backdrop-filter: blur(5px);
    }

    input[type="text"] {
      padding: 10px;
      width: 250px;
      border: none;
      border-radius: 5px;
      font-size: 1em;
    }

    input[type="submit"] {
      padding: 10px 20px;
      font-size: 1em;
      background-color: #ffffff;
      color: #2575fc;
      border: none;
      border-radius: 5px;
      margin-left: 10px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    input[type="submit"]:hover {
      background-color: #d1e1ff;
    }

    p {
      font-size: 1.2em;
      margin-top: 20px;
    }

    .error {
      color: #ffcccc;
    }

    .success {
      color: #a2ffcc;
    }
  </style>
</head>
<body>
  <h2>Enter Your Name to Get Your Seat Number</h2>
  <form method="POST">
    <input type="text" name="name" placeholder="Enter your name" required>
    <input type="submit" value="Find My Seat">
  </form>
  {% if seat %}
    <p class="success"><strong>Your Seat Number is: {{ seat }}</strong></p>
  {% elif error %}
    <p class="error"><strong>{{ error }}</strong></p>
  {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    seat = None
    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').lower()
        seat = seating.get(name)
        if not seat:
            error = "Name not found. Please check spelling."
    return render_template_string(form_html, seat=seat, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
