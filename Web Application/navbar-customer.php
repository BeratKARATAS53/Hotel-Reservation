<?php
include('db.php');
?>

<html>

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/navbar.css" />
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <div class="topnav">
        <a href="/">Home</a>
        <a href="my-reservations.php">My Reservations</a>
        <a href="settings-customer.php">Settings</a>


        <a style="float:right" href="logout.php">Log Out</a>
        <a class="active" style="float:right" href="profile-customer.php"><?php echo $_SESSION['email']; ?></a>
    </div>
</body>

</html>