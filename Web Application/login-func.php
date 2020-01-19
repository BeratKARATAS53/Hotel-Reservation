<?php
session_start();
include("db.php"); //veritabanını ekliyoruz

// giriş formundan gelen kullanıcı adı (kuladi) ve şifre(sifre) değişkenlere atıyoruz
$email = $_POST['email'];
$password = $_POST['pass'];

//kullanıcı adı ve şifeyi sorguluyoruz
$sql = "SELECT * FROM person WHERE email='$email' and passwrd='$password'";
$result = mysqli_query($baglanti, $sql);
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);

//Eğer sorgulanan kullanıcı adı var ise bir oturum oluşturup home.php ye yönlendiriyoruz
//Yok ise hata verdiriyoruz. 

if (mysqli_num_rows($result) == 1) {
    $_SESSION['email'] = $email; // Initializing Session
    header("location: home.php"); // Redirecting To Other Page
} else {
    echo "<center>" . "Your Password or E-mail Address Is Wrong!" . "</br>" . "<a href=login-page.php>TURN BACK</a>" . "</center>";
}
