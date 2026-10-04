"""Write the updated About.html into frontend/static (UTF-8).

Run from the capstone 'server' folder:
    python apply_about.py
"""
import os

TARGET = os.path.join("frontend", "static", "About.html")

HTML = """<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>About Us - Best Cars Dealership</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="/static/style.css">
  <link rel="stylesheet" href="/static/bootstrap.min.css">
</head>
<body>
<div>
  <nav class="navbar navbar-expand-lg navbar-light" style="background-color:darkturquoise; height: 1in;">
    <div class="container-fluid">
      <h2 style="padding-right: 5%;">Dealerships</h2>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" style="font-size: larger;" href="/">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" style="font-size: larger;" aria-current="page" href="/about">About Us</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="font-size: larger;" href="/contact">Contact Us</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="card" style="width: 80%; margin: auto; margin-top: 5%; margin-bottom: 5%;">
    <div class="banner" name="about-header" style="text-align: center; padding: 20px;">
      <img src="/static/cars.jpeg" alt="Cars at our dealership" style="width: 100%; max-height: 260px; object-fit: cover; border-radius: 4px;">
      <h2 style="margin-top: 15px;">About Best Cars Dealership</h2>
      <p>Best Cars is a national car retailer in the United States. Our dealerships help customers find the right vehicle, compare options and share honest reviews, so every buyer can decide with confidence. Meet the team behind the service.</p>
    </div>
    <div style="display: flex; flex-direction: row; justify-content: space-around; margin: auto; width: 100%; padding-bottom: 20px;">
      <div class="card" style="width: 30%;">
        <img class="card-img-top" src="/static/person.png" alt="Priya Sharma">
        <div class="card-body">
          <p class="title"><b>Priya Sharma</b></p>
          <p>General Manager</p>
          <p class="card-text">Priya leads the national dealership network with over 15 years in automotive retail. She focuses on transparent pricing and great customer experiences.</p>
          <p>priya.sharma@bestcars.example</p>
        </div>
      </div>

      <div class="card" style="width: 30%;">
        <img class="card-img-top" src="/static/person.png" alt="Daniel Okafor">
        <div class="card-body">
          <p class="title"><b>Daniel Okafor</b></p>
          <p>Head of Sales</p>
          <p class="card-text">Daniel manages the sales teams across all branches. He helps customers compare models and find financing that fits their budget.</p>
          <p>daniel.okafor@bestcars.example</p>
        </div>
      </div>

      <div class="card" style="width: 30%;">
        <img class="card-img-top" src="/static/person.png" alt="Maria Gonzalez">
        <div class="card-body">
          <p class="title"><b>Maria Gonzalez</b></p>
          <p>Customer Support Manager</p>
          <p class="card-text">Maria runs the support team that answers customer questions and reviews feedback. She makes sure every review is read and acted on.</p>
          <p>maria.gonzalez@bestcars.example</p>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>
"""

with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
    f.write(HTML)

print("Wrote", TARGET)
