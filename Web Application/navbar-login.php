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
        <a href="#news">News</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>

        <a style="float:right" href="profile-page.php"><?php echo $_SESSION['email']; ?></a>
        <a style="float:right" href="logout.php">Log Out</a>
    </div>
</body>

</html>