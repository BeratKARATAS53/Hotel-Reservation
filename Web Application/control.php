<?php
session_start();
//veritabanı bağlantımızı yapıyoruz
include('db.php');

//login-func.php de oluşturulan email'i burada $user_check değişkenine atıyoruz
$user_check = $_SESSION['email'];

//$user_check değişkenini burada person tablosundan email sütununda sorguluyoruz
$sql = mysqli_query($baglanti, "SELECT * FROM person WHERE email='$user_check' ");

$row = mysqli_fetch_array($sql, MYSQLI_ASSOC);

$login_user = $row['email'];

// eğer $user_check değişkeni tanımlı ise home-login sayfamız açık kalıcak eğer tanımlı değilse home-not-login 'e yönlendirecek
if (!isset($user_check)) {
    header("Location: home-login.php");
} else {
    header("Location: home-not-login.php");
}
