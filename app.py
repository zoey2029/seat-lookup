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
<title>Seat Lookup</title>
<h2>Enter Your Name to Get Your Seat Number</h2>
<form method="POST">
  Name: <input type="text" name="name">
  <input type="submit" value="Find My Seat">
</form>
{% if seat %}
  <p><strong>Your Seat Number is: {{ seat }}</strong></p>
{% elif error %}
  <p style="color:red;">{{ error }}</p>
{% endif %}
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
