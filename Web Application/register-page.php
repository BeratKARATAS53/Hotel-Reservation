<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Register Page</title>
  <link rel="stylesheet" href="css/style.css" />
</head>

<body>
  <div class="form">
    <center class="title">
      <p>REGISTER FORM</p>
    </center>
    <form id="form1" name="form1" action="register-func.php" method="post">
      <input type="text" name="first" id="first" placeholder="First Name" />
      <input type="text" name="last" id="last" placeholder="Last Name" />
      <input type="email" name="mail" id="mail" placeholder="Mail" />
      <input type="text" name="address" id="address" placeholder="Address" />
      <input type="password" name="pass" id="pass" placeholder="Password" />
      <input type="password" name="confirm-pass" id="confirm-pass" placeholder="Confirm Password" />
      <input type="text" name="phone" id="phone" placeholder="Telephone" />
      <input type="text" name="age" id="age" placeholder="Age" />
      <input type="text" name="username" id="username" placeholder="Username" />
      <input type="text" name="money" id="money" placeholder="Money" />
      <input type="text" name="hotel-name" id="hotel-name" placeholder="Hotel Name" /><br>
      <h3>Person Type</h3>
      <label class="container">Customer
        <input type="radio" name="type" id="customer" value="customer">
        <span class="checkmark"></span>
      </label>
      <label class="container">Employee
        <input type="radio" name="type" id="employee" value="employee">
        <span class="checkmark"></span>
      </label>
      <label class="container">Manager
        <input type="radio" name="type" id="manager" value="manager">
        <span class="checkmark"></span>
      </label>
      <label>&nbsp;</label>
      <input type="submit" name="submit" id="submit" value="SAVE">
    </form>
    <center>
      <p>&nbsp;</p>
      <p><a href="login-page.php">Are You Member ?, Log In</a></p>
    </center>
  </div>
</body>

</html>