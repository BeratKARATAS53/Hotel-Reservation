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
        <a href="/">Home</a>
        <a href="update.php">Update</a>
        <a href="balance-update.php">Balance</a>


        <a style="float:right" href="logout.php">Log Out</a>
        <a class="active" style="float:right" href="profile-customer.php"><?php echo $_SESSION['email']; ?></a>
    </div>
</body>

</html>