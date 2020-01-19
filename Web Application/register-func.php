<?php
//veritabanı bağlantımızı yaptık
include('db.php');
//veritabanı bağlantısı sağlanmaz ise hata verdirdik
if (mysqli_connect_errno()) {
    echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}

//kayit.php de ki formdan gelen kuladi ve sifre post verilerini $kuladi ve $sifre değişkenlerine eşitledik
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
$hotelname = $_POST['hotel-name'];
$type = $_POST['type'];

//Kayıt işlemini gerçekleştiriyoruz veritabanındaki kullaniciadi ve sifre yi formdan gelen değişkene atadığımız verilere eşitliyoruz
$kayit = "CALL addPerson('$first','$last','$pass','$email','$address','$phone',$age,$money,'$username','$hotelname','$type')";

$sonuc = mysqli_query($baglanti, $kayit);

//kayıt işlemi bitince login-page.php ye yönlendiriyoruz
header("Location: login-page.php");
