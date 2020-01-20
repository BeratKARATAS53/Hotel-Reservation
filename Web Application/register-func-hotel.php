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
$money = $_POST['money'];
$hotelname = $_POST['hotel-name'];
$type = $_POST['type'];

// Kayıt İşlemi
$kayit = "CALL addPerson('$first','$last','$pass','$email','$address','$phone',0,$money,'null','$hotelname','$type')";

$sonuc = mysqli_query($baglanti, $kayit);

if ($sonuc) {
    header("Location: login-page.php");
} else {
    header("Location: register-page-customer.php");
    echo "<center>" . "Bilgileri Kontrol edin" . "</br>" . "</center>";
}
// 
