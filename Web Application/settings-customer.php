<?php
// veritabanı bağlantımızı yaptık
include('db.php');
// veritabanı bağlantısı sağlanmaz ise hata verdirdik
if (mysqli_connect_errno()) {
    echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}

session_start();
$email = $_SESSION['email'];
$sql = "SELECT * FROM customer_all_info cai WHERE cai.email='$email'";
$result = mysqli_query($baglanti, $sql);
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
$id = $row["id"];
$age = $row["age"];
$balance = $row["money"];
$username = $row["username"];
$type = $row["p_role"];

?>

<html>

<head>
    <title>Settings Page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" , charset="utf-8">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>

<body>

    <body>
        <?php
        session_start();
        include('navbar-customer.php');
        ?>

        <div class="w3-cell-row">
            <div class="w3-container">
                <?php
                if (isset($_POST['submit'])) {
                    // Register Sayfasından Gelen Bilgileri Değişkenlere Aktarma.
                    $first = $_POST['first'];
                    $last = $_POST['last'];
                    $address = $_POST['address'];
                    $pass = $_POST['pass'];
                    $phone = $_POST['phone'];
                    $money = $_POST['money'];

                    $first =  trim($first);
                    $last =  trim($last);
                    $address =  trim($address);
                    $pass = trim($pass);
                    $phone =  trim($phone);

                    $balance = $balance + $money;

                    // Kayıt İşlemi
                    $kayit = "CALL updateperson($id,'$first','$last','$pass','$email','$address','$phone',$age,$balance,'$username','null','$type')";

                    $sonuc = mysqli_query($baglanti, $kayit);

                    if ($sonuc) {
                        echo "<script>alert('Success!');</script>";
                        // header("Location: profile-customer.php");
                    } else {
                        echo "<script>alert('All Field Are Required!');</script>";
                    }
                }

                ?>
            </div>
        </div>
        <div class="w3-cell-row" style="margin: 10px">
            <div class="w3-container w3-cell" style="width: 30%; background: linear-gradient(to right, #6190e8, #a7bfe8);">
                <h2 style="width:80%; margin-top: 10; margin-left: 70; color:#243b55"><b>Settings</b></h2>
                <div class="newForm">
                    <form method="post">
                        <input type="text" name="username" id="username" placeholder="<?php echo $username ?>" disabled />
                        <input type="text" name="first" id="first" placeholder="First Name" />
                        <input type="text" name="last" id="last" placeholder="Last Name" />
                        <input type="email" name="mail" id="mail" placeholder="<?php echo $email ?>" disabled />
                        <input type="text" name="address" id="address" placeholder="Address" />
                        <input type="password" name="pass" id="pass" placeholder="Password" />
                        <input type="text" name="phone" id="phone" placeholder="Telephone" />
                        <input type="number" name="money" id="money" placeholder="Money" /><br>
                        <label>&nbsp;</label>
                        <input type="submit" style="width:100%" name="submit" id="submit" value="SAVE">
                    </form>
                </div>
            </div>
        </div>
    </body>

</html>