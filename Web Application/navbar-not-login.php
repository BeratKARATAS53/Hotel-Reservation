<?php
include('db.php');
?>

<html>

<head>
    <meta charset="utf-8">
    <title>Member Page</title>
    <link rel="stylesheet" href="css/navbar.css" />
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <div class="topnav">
        <a class="active" href="home-login.php">Home</a>
        <a href="rooms.php">Rooms</a>
        <a href="hotels.php">Hotels</a>

        <a style="float:right" href="register-customer.php">Register</a>
        <a style="float:right;" href=" login.php">Login</a>

        <form style="float:right; margin-right: 20px" method="post">
            <input type="text" name="search" placeholder="Search">
            <input type="submit" name="submit" value="Search" style="width: 25%">
        </form>
    </div>
</body>

</html>