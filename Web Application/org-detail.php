<?php
require('db.php');
?>

<!DOCTYPE html>
<html>

<head>
    <title>Organization Detail</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <?php
    session_start();
    include("navbar.php");

    $id = $_GET['id'];

    $org_query = "SELECT * FROM organization WHERE id = $id ORDER BY id desc";
    $result_org = mysqli_query($baglanti, $org_query);

    $row_org = mysqli_fetch_array($result_org, MYSQLI_ASSOC);
    $org_price = $row_org["price"];

    session_start();
    $email = $_SESSION['email'];
    $customer_query = "SELECT * FROM customer_all_info c WHERE c.email='$email'";
    $customer_result = mysqli_query($baglanti, $customer_query);
    $customer_row = mysqli_fetch_array($customer_result, MYSQLI_ASSOC);

    $c_id = $customer_row["customer_id"];
    $c_balance = $customer_row["money"];

    if (isset($_POST['reserve'])) {
        if ($customer_result != 0) {
            if ($c_balance < $org_price) {
                echo "<script>alert('Your balance is not enough for reservation!');</script>";
            } else {
                $kayit = "CALL addrentorganization($c_id,$id)";
                $sonuc = mysqli_query($baglanti, $kayit);

                if ($sonuc) {
                    echo "<script>alert('Rent to Organization, Successfully!');</script>";
                } else {
                    header("Location: login.php");
                }
            }
        }
    }


    ?>
    <div class="w3-cell-row" style="margin: 50px">
        <div class="w3-container">
            <div style="width:100%; font-size: 15; margin: auto; margin-top: 50">
                <header class="w3-container w3-light-grey">
                    <h4> <?php echo $row_org["name"] ?> </h4>
                </header>
                <div class="w3-container">
                    <img src="css/image/img-<?php echo $row_org["image"] ?>" alt="Organization Image" height="250" width="300">
                    <p>
                        <?php echo "Organization Information: ", $row_org["org_info"] . "<br/>",
                            "Hotel Name: ",
                            $row_org["name"]  . "<br/>"
                        ?>
                    </p>
                </div>
                <hr>
                <p>
                    Total Price: <input type="text" name="totalPrice" value="<?php echo $row_org["price"] . " $"  ?>" disabled />
                    Your Balance: <input type="text" name="balance" value="<?php echo $c_balance . " $"  ?>" disabled />
                </p>
                <form method="post">
                    <?php
                    if ($row_org["price"] <= $c_balance) { ?>
                        <input type="submit" name="reserve" value="Reservation" />
                    <?php } else { ?>
                        <h6 style="color: red"> Your balance is not enough for rent organization! </h6>
                    <?php }
                    ?>
                </form>
                <hr>
            </div>
        </div>
    </div>
</body>

</html>