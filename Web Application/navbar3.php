<?php
include('db.php');

$user = $_SESSION["login_user"];
echo $user;
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

        <?php
        $user = $_SESSION["email"];
        if ($user) { ?>
            <a style="float:right" href="logout.php">Log Out</a>
            <a style="float:right" href="profile-page.php"><?php echo $user; ?></a>
        <?php
        } else { ?>
            <a style="float:right" href="login.php">Login</a>
            <a style="float:right" href="register-customer.php">Register</a>
        <?php } ?>
      
    </div>
</body>

</html>