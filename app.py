from flask import Flask, request, render_template_string

app = Flask(__name__)

students = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Result Management System</title>
    <style>
        body{
            font-family:Arial, sans-serif;
            background:#f2f2f2;
            margin:40px;
        }
        .container{
            width:500px;
            margin:auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0 0 10px gray;
        }
        input{
            width:100%;
            padding:10px;
            margin:8px 0;
        }
        input[type=submit]{
            background:#28a745;
            color:white;
            border:none;
            cursor:pointer;
        }
        table{
            width:100%;
            margin-top:20px;
            border-collapse:collapse;
        }
        table,th,td{
            border:1px solid black;
        }
        th,td{
            padding:10px;
            text-align:center;
        }
        th{
            background:#28a745;
            color:white;
        }
    </style>
</head>

<body>

<div class="container">

<h2 align="center">Student Result Management System</h2>

<form method="POST">

<input type="text" name="name" placeholder="Student Name" required>

<input type="text" name="roll" placeholder="Roll Number" required>

<input type="number" name="marks" placeholder="Marks" min="0" max="100" required>

<input type="submit" value="Add Student">

</form>

{% if students %}

<table>

<tr>
<th>Name</th>
<th>Roll No</th>
<th>Marks</th>
<th>Result</th>
</tr>

{% for s in students %}

<tr>
<td>{{ s["name"] }}</td>
<td>{{ s["roll"] }}</td>
<td>{{ s["marks"] }}</td>
<td>{{ s["result"] }}</td>
</tr>

{% endfor %}

</table>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name")
        roll = request.form.get("roll")
        marks = int(request.form.get("marks"))

        if marks >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        students.append({
            "name": name,
            "roll": roll,
            "marks": marks,
            "result": result
        })

    return render_template_string(html, students=students)


if __name__ == "__main__":
    app.run(debug=True)