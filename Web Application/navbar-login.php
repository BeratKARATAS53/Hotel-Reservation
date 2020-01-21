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

        <a style="float:right" href="profile-page.php"><?php echo $_SESSION['email']; ?></a>
        <a style="float:right" href="logout.php">Log Out</a>
        <?php
        include("search.php");
        /*
        if ((include("control.php"))) { ?>
            <a style="float:right" href="profile-page.php"><?php echo $_SESSION['email']; ?></a>
            <a style="float:right" href="logout.php">Log Out</a>
        <?php
        } else { ?>
            <a style="float:right" href="login-page.php">Login</a>
            <a style="float:right" href="register-page-customer.php">Register</a>
        <?php } */ ?>
    </div>
</body>

</html>