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
$confpass = $_POST['confirm-pass'];
$phone = $_POST['phone'];
$age = $_POST['age'];
$username = $_POST['username'];
$money = $_POST['money'];

// Kayıt İşlemi
$kayit = "CALL addPerson('$first','$last','$pass','$email','$address','$phone',$age,$money,'$username','null','customer')";

$sonuc = mysqli_query($baglanti, $kayit);

if ($sonuc) {
    header("Location: login-page.php");
} else {
    header("Location: register-page-customer.php");
    echo "<center>" . "Bilgileri Kontrol edin" . "</br>" . "</center>";
}
// 
