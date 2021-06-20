<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width:device-width, initial-scale:1.0">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css\master.css">
  <title>Prognosis Prediction</title>
</head>
<style>
  img {
    border-radius: 50%;
  }
  </style>
<body>
  <section id="top-intro" class="top-intro">
    <div class="container-fluid">
      <nav class="navbar navbar-expand-lg navbar-dark">
          <div class="logo" ><img src="static/logo.png" alt="logo" width="80" height="80"></div>
        <a class="navbar-brand" href="" style="text-shadow: 1px 1px #c0c0c0; font-size: 40px;"><b>Disease Predictor</b></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a class="nav-link" href="#about" style="text-shadow: 1px 1px #c0c0c0;">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="login.php" style="text-shadow: 1px 1px #c0c0c0;">Login </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="signup.php" style="text-shadow: 1px 1px #c0c0c0;">Sign up </a>
            </li>
          </ul>
        </div>
      </nav>

      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-6">
          <h2 class="main-heading">Hello there...<br>Welcome aboard!</h2>
        </div>
        <div>
            <style>
                .pred_btn:link, .pred_btn:visited {
                  background-color:transparent;
                  color: rgb(252, 252, 252);
                  border: 2px solid #fff;
                  padding: 10px 20px;
                  position: absolute;
                  font-size: 30px;
                  font-weight: bold;
                  text-align: center;
                  text-decoration: none;
                  display: inline-block;
                  top: 58%;
                  left: 40%;

                }
                </style>
       <a class="pred_btn" href="login.php"><b>Enter your symptoms →</b></a>
       </div>


      </div>
      </div>
  </section>

  <section id="about" class="about">
    <h1 class="text">ABOUT US</h2>
    <br><br><br><br>
    <p>This is a <strong>Disease Predicting System </strong>that takes symptoms as input from the patients. <br>
    The symptoms submitted by a patient/ user will act as the input to a machine learning model that can predict diseases based on them. This website not only predicts the disease, but also suggests specialization that is meant to deal with the prognosis and some relevant information about the same.
    </p>
  </section>

  <section class="bottom">
    <footer id="footer" class="footer">

      <p>Disease Prediction System | The Trojan Squad</p><br>
      <a href="#top-intro" style="text-decoration:none; color : white">Back to top</a>

    </footer>
  </section>


</body>
</html>
