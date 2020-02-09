<?php
// veritabanı bağlantımızı yaptık
include('db.php');
// veritabanı bağlantısı sağlanmaz ise hata verdirdik
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
$age = $_POST['age'];
$username = $_POST['username'];
$money = $_POST['money'];

$first =  trim($first);
$last =  trim($last);
$email = trim($email);
$address =  trim($address);
$pass = trim($pass);
$phone =  trim($phone);
$age =  trim($age);
$username =  trim($username);
$money =  trim($money);

// Kayıt İşlemi
$kayit = "CALL addPerson('$first','$last','$pass','$email','$address','$phone',$age,$money,'$username','null','null','customer')";

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
      <p>CUSTOMER REGISTER FORM</p>
      <p><a href="register-hotel.php">Go To Hotel Employee Register >>></a></p>
    </center>
    <form method="post">
      <input type="text" name="first" id="first" placeholder="First Name" />
      <input type="text" name="last" id="last" placeholder="Last Name" />
      <input type="email" name="mail" id="mail" placeholder="Mail" />
      <input type="text" name="address" id="address" placeholder="Address" />
      <input type="password" name="pass" id="pass" placeholder="Password" />
      <input type="text" name="phone" id="phone" placeholder="Telephone" />
      <input type="text" name="age" id="age" placeholder="Age" />
      <input type="text" name="username" id="username" placeholder="Username" />
      <input type="text" name="money" id="money" placeholder="Money" />
      <label>&nbsp;</label>
      <input type="submit" name="submit" id="submit" value="SAVE">
    </form>
    <center>
      <p><a href="login.php">Are You Member? Log In</a></p>
    </center>
  </div>
</body>

</html>