<?php
session_start();
//veritabanı bağlantımızı yapıyoruz
include('db.php');

//girisisle.php de oluşturulan username mi burada $user_check değişkenine atıyoruz
$user_check = $_SESSION['email'];

//$user_check değişkenini burada uye tablosundan kullaniciadi hücresinde sorguluyoruz
$sql = mysqli_query($baglanti, "SELECT * FROM person WHERE email='$user_check' ");

$row = mysqli_fetch_array($sql, MYSQLI_ASSOC);

$login_user = $row['email'];

/* eğer $user_check değikeni tanımlı ise home.php sayfamız
açık kalıcak eğer tanımlı değilse login-page.php ye yönlendirecek */
if (!isset($user_check)) {
    header("Location: login-page.php");
}
