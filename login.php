<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Login Page</title>
    <link rel="stylesheet" type="text/css" href="loginstyle.css" />
  </head>
  <body>
    <div class="title"><h1>Sign In Form</h1></div>
    <div class="container">
      <div class="left">
        <h1>WELCOME!<h2>
        <h2> Please Log in here </h2>
      </div>
      <div class="right">
        <div class="formBox">
          <form method="post">
            <label for="usrname" style="color: white;">Email</label>
            <input
              type="text"
              id="usrname"
              name="usrname"
              placeholder="Email id"
              onchange="onChangeUsername(this.value)"
              required
            />
            <label for="psw" style="color: white;">Password</label>
            <input
              type="Password"
              id="psw"
              name="psw"
              placeholder="*******"
              onchange="onChangePassword(this.value)"
              required
            />
            <a href="#" style="color: white;">Forgot Password</a><br><br>
            <input
              type="submit"
              name="submit"
              value="Sign in"
            />
            <!-- onclick="location.href='signup.html'" -->
            <input
              type="submit"
              name=""
              value="Sign up"
              onclick="location.href='signup.php'"
              required
            />
          </form>
        </div>
      </div>
    </div>
    <?php
      $con = mysqli_connect("localhost", "root", "","hackbout");
      if(!$con){
        die("Could not connect: " . mysqli_connect_error());
      }


if($_SERVER['REQUEST_METHOD'] === 'POST')
{

    $sql = "SELECT * FROM signup WHERE email = '$_POST[usrname]' AND password = '$_POST[psw]'";
    $result = mysqli_query($con,$sql);
    $rows = mysqli_num_rows($result);

    if(!mysqli_query($con,$sql))
    {
      die('Error: ' . mysqli_error());
    }

    if($rows != 0)
    {
      header("location:http://127.0.0.1:5000");
    }
    else
    {
      echo"<script>alert('Incorrect username or password');</script>";
      //die();
    }

}

      if($_SERVER['REQUEST_METHOD'] === 'POST') {
        if(isset($_POST['submit'])) {
          $sql = "INSERT INTO login (username, password )
          VALUES('$_POST[usrname]','$_POST[psw]')";

          if(!mysqli_query($con,$sql)) {
            die("Error: ".mysqli_error($con));
          }
          echo "<script>alert('Logging you in...');</script>";
        }
      }
      mysqli_close($con);
    ?>
  </body>
</html>