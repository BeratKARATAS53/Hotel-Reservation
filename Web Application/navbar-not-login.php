<?php
include('db.php');
?>

<html>

<head>
    <meta charset="utf-8">
    <title>Member Page</title>
    <link rel="stylesheet" href="css/navbar.css" />
</head>

<body>
    <div class="topnav">
        <a class="active" href="home-login.php">Home</a>
        <a href="rooms.php">Rooms</a>
        <a href="hotels.php">Hotels</a>

        <?php
        include("search.php"); ?>

        <a style="float:right" href="login-page.php">Login</a>
        <a style="float:right" href="register-page-customer.php">Register</a>
    </div>
</body>

</html>