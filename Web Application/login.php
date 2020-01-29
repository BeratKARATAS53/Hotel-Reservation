<?php

session_start();

include("db.php"); //veritabanını ekliyoruz

if (isset($_POST['email']) && isset($_POST['pass'])) //when form submitted
{
    $email = $_POST['email'];
    $password = $_POST['pass'];

    $email = trim($email);
    $password = trim($password);

    $password = md5($password);

    $sql = "SELECT * FROM person WHERE email='$email' and passwrd='$password'";
    $result = mysqli_query($baglanti, $sql);
    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);

    if (mysqli_num_rows($result) == 1) {
        $_SESSION['email'] = $email;
        if (($row["p_role"] == "manager") || ($row["p_role"] == "employee")) {
            header('Location: profile-employees.php'); //redirect to profile page
        } else {
            header('Location: /'); //redirect to main
        }
    } else {
        echo "<script>alert('Wrong login or password');</script>" . $sql;
    }
}

?>

<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <title>Login Page</title>
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <div class="newForm">
        <center class="newTitle">
            <p>LOGIN</p>
        </center>
        <form method="post">
            <input type="email" name="email" id="email" placeholder="Mail" />
            <input type="password" name="pass" id="pass" placeholder="Password" />
            <label>&nbsp;</label>
            <input type="submit" name="submit" id="submit" value="LOGIN">
        </form>
        <center><a href="register-customer.php"><br>
                Aren't You Member? Register</a></center>
    </div>
</body>

</html>