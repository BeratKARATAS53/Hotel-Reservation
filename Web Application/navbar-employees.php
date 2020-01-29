<?php
include('db.php');
?>

<html>

<head>
    <meta charset="utf-8">
    <title>Hotel Employee Page</title>
    <link rel="stylesheet" href="css/navbar.css" />
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <div class="topnav">
        <a class="active" href="profile-employees.php">Home</a>
        <a href="hotel-settings.php">Settings</a>
        <a href="hotel-balance.php">Balance</a>
        <a href="statistics.php">Statistics</a>

        <?php
        $user = $_SESSION["email"];
        if ($user) { ?>

            <a href="add-room.php">Add Room</a>
            <a href="add-organization.php">Add Organization</a>
            <a style="float:right" href="logout.php">Log Out</a>
            <a style="float:right" href="profile-employees.php"><?php echo $user; ?></a>
        <?php
        } else { ?>
            <a style="float:right" href="login.php">Login</a>
            <a style="float:right" href="register-customer.php">Register</a>
        <?php } ?>
    </div>
</body>

</html>