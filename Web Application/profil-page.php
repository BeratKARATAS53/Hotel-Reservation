<?php
require('db.php');
?>
<html>

<head>
   <meta charset="utf-8">
   <title>Member Page</title>
   <link rel="stylesheet" href="css/style.css" />
   <link rel="stylesheet" href="css/navbar.css" />
</head>

<body>
   <?php
   session_start();
   $email = $_SESSION['email'];
   include('navbar-login2.php');
   $sql = "SELECT * FROM person WHERE email='$email';";
   $result = mysqli_query($baglanti, $sql);
   $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
   ?>

   <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
      <header class="w3-container w3-light-grey">
         <h4> <?php echo $row["firstname"] ?> </h4>
      </header>
      <div class="w3-container">
         <p><?php echo "First Name: ", $row["firstname"], "<br/>",
               "Last Name: ",
               $row["lastname"] . "<br/>",
               "Email: ",
               $row["email"] . "<br/>",
               "Address: ",
               $row["address"] . "<br/>",
               "Telephone: ",
               $row["telephone"],
               "<br/>" ?></p>



</body>

</html>