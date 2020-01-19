<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Login Page</title>
  <link rel="stylesheet" href="css/style.css" />
</head>

<body>
  <div class="form">
    <center class="title">
      <p>LOGIN</p>
    </center>
    <form id="form1" name="form1" action="login-func.php" method="post">
      <input type="email" name="email" id="email" placeholder="Mail" />
      <input type="password" name="pass" id="pass" placeholder="Password" />
      <label>&nbsp;</label>
      <input type="submit" name="submit" id="submit" value="LOGIN">
    </form>
    <center><a href="register-page.php"><br>
        Aren't You Member? Register</a></center>
  </div>
</body>

</html>