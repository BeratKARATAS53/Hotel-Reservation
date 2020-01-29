<?php
require('db.php');
?>
<html>

<head>
   <title>Hotel Employees Page</title>
   <meta name="viewport" content="width=device-width, initial-scale=1" , charset="utf-8">
   <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>

<body>
   <?php
   session_start();
   $email = $_SESSION['email'];
   include('navbar-employees.php');
   $sql = "SELECT * FROM person WHERE email='$email';";
   $result = mysqli_query($baglanti, $sql);
   $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
   ?>

   <div class="w3-cell-row" style="margin: 50px">
      <div class="w3-container w3-red w3-cell" style="width: 25%; background: linear-gradient(to right, #6190e8, #a7bfe8);">
         <h2 style="width:80%; margin: auto; margin-top: 50"></h2>
      </div>
      <div class="w3-container">
         <h2 style="width:80%; margin: auto; margin-top: 50">Staff</h2>

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
                     $row["telephone"] . "<br/>",
                     "Role: ",
                     $row["p_role"] . "<br/>" ?></p>
            </div>
         </div>
      </div>
   </div>


</body>

</html>