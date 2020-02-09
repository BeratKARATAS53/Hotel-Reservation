<?php
include('db.php');

$user = $_SESSION["login_user"];
echo $user;
?>

<html>

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/navbar.css" />
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <div class="topnav">
        <a class="active" href="/">Home</a>
        <a href="rooms.php">Rooms</a>
        <a href="hotels.php">Hotels</a>
        <a href="organizations.php">Organizations</a>

        <?php
        $user = $_SESSION["email"];
        if ($user) { ?>
            <a style="float:right" href="logout.php">Log Out</a>
            <a style="float:right" href="profile-customer.php"><?php echo $user; ?></a>
        <?php
        } else { ?>
            <a style="float:right" href="login.php">Login</a>
            <a style="float:right" href="register-customer.php">Register</a>
        <?php } ?>
        <form style="float:right; margin-right: 20px" method="post">
            <input type="text" name="search" placeholder="Search">
            <input type="submit" name="submit" value="Search" style="width: 25%">
        </form>
    </div>
</body>

</html>