<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Registration</title>
    <style>
        body {
            background-image: url('/static/img/new_background.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            font-family: Arial, sans-serif;
        }
        .container {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            max-width: 500px;
            margin: auto;
            text-align: center;
        }
        h1, h2 {
            color: #333;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input[type="text"], input[type="number"], input[type="email"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #f2f2f2;
            margin: 5px 0;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Student Registration</h1>
        <form action="/add" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required><br>
            <label for="grade">Grade:</label>
            <input type="text" id="grade" name="grade" required><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>
            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required><br>
            <input type="submit" value="Add Student">
        </form>
        
        <h2>Registered Students</h2>
        <ul>
            {% for student in students %}
                <li>{{ student.name }} - {{ student.age }} - {{ student.grade }} - {{ student.email }} - {{ student.address }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
