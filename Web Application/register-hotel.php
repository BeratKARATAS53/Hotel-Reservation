<?php
//veritabanı bağlantımızı yaptık
include('db.php');
//veritabanı bağlantısı sağlanmaz ise hata verdirdik
if (mysqli_connect_errno()) {
  echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}

// Register Sayfasından Gelen Bilgileri Değişkenlere Aktarma.
$first = $_POST['first'];
$last = $_POST['last'];
$email = $_POST['mail'];
$address = $_POST['address'];
$pass = $_POST['pass'];
$phone = $_POST['phone'];
$money = $_POST['money'];
$hotelname = $_POST['hotel-name'];
$type = $_POST['type'];

$first =  trim($first);
$last =  trim($last);
$email = trim($email);
$address =  trim($address);
$pass = trim($pass);
$phone =  trim($phone);
$money =  trim($money);
$hotelname =  trim($hotelname);

// Kayıt İşlemi
$kayit = "CALL addPerson('$first','$last','$pass','$email','$address','$phone',0,$money,'null','$hotelname','null','$type')";

$sonuc = mysqli_query($baglanti, $kayit);

if ($sonuc) {
  header("Location: login.php");
} else {
  echo "<script>alert('All Field Are Required!');</script>";
}

?>

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
      <p><a href="register-customer.php">Go To Customer Register >>></a></p>
    </center>
    <form method="post">
      <input type="text" name="first" id="first" placeholder="First Name" />
      <input type="text" name="last" id="last" placeholder="Last Name" />
      <input type="email" name="mail" id="mail" placeholder="Mail" />
      <input type="text" name="address" id="address" placeholder="Address" />
      <input type="password" name="pass" id="pass" placeholder="Password" />
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
      <p><a href="login.php">Are You Member ?, Log In</a></p>
    </center>
  </div>
</body>

</html>