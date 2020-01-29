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
        <a href="home-login.php">Home</a>
        <a href="update.php">Update</a>
        <a href="balance-update.php">Balance</a>


        <a style="float:right" href="logout.php">Log Out</a>
        <a class="active" style="float:right" href="profil-page.php"><?php echo $_SESSION['email']; ?></a>
		
		<form style="float:right; margin-right: 20px" method="post">
            <input type="text" name="search" placeholder="Search">
            <input type="submit" name="submit" value="Search" style="width: 25%">
        </form>
		
	</div>
	
</body>

</html>



