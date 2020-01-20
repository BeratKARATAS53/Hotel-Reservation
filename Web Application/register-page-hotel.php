<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Register Page</title>
  <link rel="stylesheet" href="css/style.css" />
</head>

<body>
  <div class="newForm">
    <center class="newTitle">
      <p>HOTEL EMPLOYEE REGISTER FORM</p>
      <p><a href="register-page-customer.php">Go To Customer Register >>></a></p>
    </center>
    <form id="form1" name="form1" action="register-func-hotel.php" method="post">
      <input type="text" name="first" id="first" placeholder="First Name" />
      <input type="text" name="last" id="last" placeholder="Last Name" />
      <input type="email" name="mail" id="mail" placeholder="Mail" />
      <input type="text" name="address" id="address" placeholder="Address" />
      <input type="password" name="pass" id="pass" placeholder="Password" />
      <input type="password" name="confirm-pass" id="confirm-pass" placeholder="Confirm Password" />
      <input type="text" name="phone" id="phone" placeholder="Telephone" />
      <input type="text" name="money" id="money" placeholder="Money" />
      <input type="text" name="hotel-name" id="hotel-name" placeholder="Hotel Name" /><br>
      <h3>Person Type</h3>
      <label class="newContainer">Employee
        <input type="radio" name="type" id="employee" value="employee">
        <span class="newCheckmark"></span>
      </label>
      <label class="newContainer">Manager
        <input type="radio" name="type" id="manager" value="manager">
        <span class="newCheckmark"></span>
      </label>
      <label>&nbsp;</label>
      <input type="submit" name="submit" id="submit" value="SAVE">
    </form>
    <center>
      <p><a href="login-page.php">Are You Member ?, Log In</a></p>
    </center>
  </div>
</body>

</html>