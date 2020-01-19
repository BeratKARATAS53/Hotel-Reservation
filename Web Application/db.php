<?php

// Veritabani baglantimizi yapiyoruz
$host = "localhost";
$user = "root";
$pass = "password";
$db = "hotel_reservation";

$baglanti = mysqli_connect($host, $user, $pass, $db);
if (mysqli_connect_errno()) {
    echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}
