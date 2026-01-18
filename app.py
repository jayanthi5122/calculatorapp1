from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
        <input type="number" step="any" name="a" placeholder="First number" required><br><br>
        <input type="number" step="any" name="b" placeholder="Second number" required><br><br>

        <select name="choice" required>
            <option value="1">Add</option>
            <option value="2">Subtract</option>
            <option value="3">Multiply</option>
            <option value="4">Divide</option>
        </select><br><br>

        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        choice = request.form["choice"]

        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            result = "Error: Division by zero" if b == 0 else a / b

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
    
from utils import add, subtract, multiply, divide

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

