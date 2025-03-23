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
  <title>Wedding Seat Lookup</title>
  <style>
    body {
      background: linear-gradient(to right, #fbc2eb, #a6c1ee);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #333;
      text-align: center;
      padding-top: 50px;
    }

    h2 {
      font-size: 2.2em;
      margin: 20px 0 30px;
    }

    form {
      background: rgba(255, 255, 255, 0.8);
      padding: 30px;
      border-radius: 15px;
      display: inline-block;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    input[type="text"] {
      padding: 12px;
      width: 250px;
      border: 2px solid #ccc;
      border-radius: 8px;
      font-size: 1em;
      margin-bottom: 15px;
    }

    input[type="submit"] {
      padding: 12px 20px;
      font-size: 1em;
      background-color: #ff9a9e;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.3s;
    }

    input[type="submit"]:hover {
      background-color: #f67280;
    }

    p {
      font-size: 1.2em;
      margin-top: 20px;
    }

    .error {
      color: #c0392b;
    }

    .success {
      color: #27ae60;
    }

    /* Animation container */
    .animation-container {
      margin-bottom: 30px;
    }
  </style>
</head>
<body>

  <div class="animation-container">
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player 
        src="https://lottie.host/6ed38130-31ed-468d-a21b-cd8f51851fcf/JLwGC4TReY.json"  
        background="transparent"  
        speed="1"  
        style="width: 200px; height: 200px; margin: 0 auto;"  
        loop  
        autoplay>
    </lottie-player>
  </div>

  <h2>Welcome to the Wedding Seat Lookup</h2>
  <form method="POST">
    <input type="text" name="name" placeholder="Enter your name" required><br>
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
