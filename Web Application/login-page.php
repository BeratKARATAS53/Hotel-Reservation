<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Login Page</title>
</head>

<body>
  <center>
    <p>LOGIN</p>
  </center>
  <form id="form1" name="form1" action="login-func.php" method="post">
    <table width="259" border="0" align="center">
      <tbody>
        <tr>
          <td width="96">Email</td>
          <td width="153"><input type="text" name="email" id="email"></td>
        </tr>
        <tr>
          <td>Password</td>
          <td><input type="text" name="pass" id="pass"></td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td><input type="submit" name="submit" id="submit" value="LOGIN"></td>
        </tr>
      </tbody>
    </table>
  </form>
  <center><a href="register-page.php"><br>
      REGISTER</a></center>
</body>

</html>