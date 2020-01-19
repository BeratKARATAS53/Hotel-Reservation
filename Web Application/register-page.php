<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Register Page</title>
</head>

<body>
  <center>
    <p>REGISTER FORM</p>
  </center>
  <form id="form1" name="form1" action="register-func.php" method="post">
    <table width="500" border="0" align="center">
      <tbody>
        <tr>
          <td width="%25">First Name</td>
          <td width="%25"><input type="text" name="first" id="first"></td>
          <td width="%25">Last Name</td>
          <td width="%25"><input type="text" name="last" id="last"></td>
        </tr>
        <tr>
          <td width="96">Email</td>
          <td width="300"><input type="text" name="mail" id="mail"></td>
          <td width="96">Address</td>
          <td width="153"><input type="text" name="address" id="address"></td>
        </tr>
        <tr>
          <td width="96">Şifre</td>
          <td><input type="text" name="pass" id="pass"></td>
          <td width="196">Şifre (Tekrardan)</td>
          <td><input type="text" name="confirm-pass" id="confirm-pass"></td>
        </tr>
        <tr>
          <td width="96">Phone</td>
          <td width="100"><input type="text" name="phone" id="phone"></td>
          <td width="96">Age</td>
          <td width="25"><input type="text" name="age" id="age"></td>
        </tr>
        <tr>
          <td width="96">Username</td>
          <td width="153"><input type="text" name="username" id="username"></td>
          <td width="96">Money</td>
          <td width="153"><input type="text" name="money" id="money"></td>
        </tr>
        <tr>
          <td width="96">Hotel Name</td>
          <td width="153"><input type="text" name="hotel-name" id="hotel-name"></td>
          <td width="96">Person Type</td>
          <td width="153"><input type="text" name="type" id="type"></td>
        </tr>
        <tr>
          <td>&nbsp;</td>
          <td><input type="submit" name="submit" id="submit" value="SAVE"></td>
        </tr>
      </tbody>
    </table>
  </form>
  <center>
    <p>&nbsp;</p>
    <p><a href="login-page.php">Are You Member ?, Log In</a></p>
  </center>
</body>

</html>