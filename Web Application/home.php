<html>

<head>
   <meta charset="utf-8">
   <title>Member Page</title>
</head>

<body>
   <?php
   /* include ettiğimiz control.php ile Sayfada oturumun açılıp açılmadığını kontrol ediyoruz eğer oturum açılmamış ise login-page.php ye yönlendiriyoruz */

   include('control.php');
   ?>
   Member Page <br />
   <p>Welcome <?php echo $_SESSION['email']; ?>!</p>
   <a href="logout.php">Log Out</a>
</body>

</html>