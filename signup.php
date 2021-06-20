<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Signup Page</title>
        <link rel="stylesheet" type="text/css" href="signupstyles.css">
    </head>
    <body>
        <div class="title"><h1>Sign Up Form</h1></div>
        <div class="container">
            <div class="left">
            <h1>WELCOME!<h2>
            <h2> Sign up </h2>
            <h3> To use all features </h3>
            </div>
            <div class="right">
                <div class="formBox">
                    <form method="post">
                        <p>Name</p>
                        <input type="text" name="name" placeholder="Type your Name" required><br>
                        <p>E-mail</p>
                        <input type="text" name="email" placeholder="Type you email id here" required><br>
                        <p>Contact Number</p>
                        <input type="tel" name="tel" placeholder= "Enter your contact number" required><br>
                        <p>Country</p>
                        <input type="text" name="country" placeholder="Type your Country" required><br>
                        <p>City</p>
                        <input type="text" name="city" placeholder="Type your City" required><br>
                        <p>Pin code</p>
                        <input type="text"  name="pin_code" placeholder="Enter your pin code"  pattern="[0-9]{6}" maxlength="6" required><br>
                        <p>Password</p>
                        <input type="Password" id="pswd2" name="pswd" placeholder="Enter a password of min 8 characters" required><br>
                        <p>Confirm Password</p>
                        <input type="Password" id="pswd1" name="cpswd" placeholder="Enter a password again" required><br><br>
                        <input type="submit" name="submit" value="Sign Up" onclick="validate()">
                    </form>
                </div>
            </div>
        </div>
        <script>
        function validate() {
            var pass1 = document.getElementById("pswd1").value;
            var pass2 = document.getElementById("pswd2").value;
            //alert(pass1);
            if(pass1 !== pass2) {
              alert('Check your password!');
              //location.href='dashboard.php';
            }
          }
        </script>

        <?php
          $con = mysqli_connect("localhost","root","","hackbout");
          if(!$con) {
            die("Error: ".mysqli_connect_error());
          }
          if($_SERVER['REQUEST_METHOD'] === "POST"){
            if(isset($_POST['submit'])) {
              $sql = "INSERT INTO signup (name, email, phno, country, city, pincode, password, confirmpassword)
              VALUES('$_POST[name]','$_POST[email]','$_POST[tel]','$_POST[country]','$_POST[city]','$_POST[pin_code]','$_POST[pswd]', '$_POST[cpswd]')";

              if(!mysqli_query($con, $sql)) {
                die('Error: '.mysqli_error($con));
              }
              echo "<script>alert('Thank you signing up!');</script>";
            }
          }
          mysqli_close($con);

        ?>

    </body>
</html>
