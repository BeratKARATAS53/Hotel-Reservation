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
        <a class="active" href="profile-employees.php">Home</a>
        <a href="settings-employees.php">Settings</a>

        <?php
        $user = $_SESSION["email"];
        if ($user) {

            $sql = "SELECT * FROM person WHERE email='$email';";
            $result = mysqli_query($baglanti, $sql);
            $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
            if ($row["p_role"] == "manager") { ?>
                <a href="add-room.php">Add Room</a>
                <a href="add-organization.php">Add Organization</a>
                <a href="statistics.php">Statistics</a>
            <?php }
            ?>
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