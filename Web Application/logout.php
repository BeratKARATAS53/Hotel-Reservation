<?php
//oturumu kapatıp login-page.php ye yönlendiriyoruz.
session_start();
if (session_destroy()) {
    header("Location: home-not-login.php");
}
