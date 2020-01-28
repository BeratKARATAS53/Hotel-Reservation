<?php
session_start();
// veritabanı bağlantımızı yapıyoruz
include('db.php');

// login.php de oluşturulan email'i burada $person_check değişkenine atıyoruz
$person_check = $_SESSION['email'];

//$person_check değişkenini burada person tablosundan email hücresinde sorguluyoruz
$sql = mysqli_query($baglanti, "SELECT * FROM person WHERE email = '$person_check'");

$row = mysqli_fetch_array($sql, MYSQLI_ASSOC);

$login_user = $row['id'];

/* eğer $person_check değişkeni tanımlı ise home.php sayfamız açık kalıcak eğer tanımlı değilse login.php ye yönlendirecek */
if (!isset($person_check)) {
    echo "Giriş Başarısız";
    // header("Location: home-not-login.php");
}
