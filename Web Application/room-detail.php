<?php
require('db.php');
?>

<!DOCTYPE html>
<html>

<head>
    <title>Room Detail</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <?php
    session_start();
    include("navbar.php");

    $id = $_GET['id'];

    $room_query = "SELECT * FROM room WHERE id = $id ORDER BY id desc";
    $result_room = mysqli_query($baglanti, $room_query);

    $row_room = mysqli_fetch_array($result_room, MYSQLI_ASSOC);
    $room_number = $row_room["room_number"];
    $room_price = $row_room["room_price"];

    $startDate = $_GET['start'];
    $finishDate = $_GET['finish'];

    $startDT = strtotime($startDate);
    $finishDT = strtotime($finishDate);
    $dateDiff = abs($finishDT - $startDT) / 60 / 60 / 24;

    $totalPrice = $room_price * $dateDiff;

    session_start();
    $email = $_SESSION['email'];
    $customer_query = "SELECT * FROM customer_all_info c WHERE c.email='$email'";
    $customer_result = mysqli_query($baglanti, $customer_query);
    $customer_row = mysqli_fetch_array($customer_result, MYSQLI_ASSOC);

    $c_id = $customer_row["customer_id"];
    $c_balance = $customer_row["money"];

    if (isset($_POST['add'])) {
        echo "This is Button1 that is selected";
    }
    if (isset($_POST['delete'])) {
        echo "This is Button2 that is selected";
    }
    if (isset($_POST['reserve'])) {
        if ($customer_result != 0) {
            if ($c_balance < $totalPrice) {
                echo "<script>alert('Your balance is not enough for reservation!');</script>";
            } else {
                $kayit = "CALL addReservation('$startDate','$finishDate',$c_id,'$room_number',$totalPrice)";
                $sonuc = mysqli_query($baglanti, $kayit);

                if ($sonuc) {
                    echo "<script>alert('Reservation, Successfully!');</script>";
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
                    <h4> <?php echo $row_room["room_info"] ?> </h4>
                </header>
                <div class="w3-container">
                    <img src="css/image/img-<?php echo $row_room["image"] ?>" alt="Room Image" height="250" width="300">
                    <p>
                        <?php echo  "Room Price: ",
                            $row_room["room_price"],
                            " $" . "<br/>",
                            "Room Number: ",
                            $row_room["room_number"] . "<br/>",
                            "Room Status: ",
                            $row_room["status"] . "<br/>",
                            "Room Capacity: ",
                            $row_room["capacity"],
                            " Person" . "<br/>"
                        ?>
                    </p>
                </div>
                <hr>
                <p>
                    Total Price: <input type="text" name="totalPrice" value="<?php echo $totalPrice . " $"  ?>" disabled />
                    Your Balance: <input type="text" name="balance" value="<?php echo $c_balance . " $"  ?>" disabled />
                </p>
                <form method="post">
                    <?php
                    if ($row_room["status"] == 'available') { ?>
                        <input type="submit" name="reserve" value="Reservation" />
                    <?php } else { ?>
                        <h6 style="color: red"> ! Since the room is under renovation, it is not possible to rent it ! </h6>
                    <?php }
                    ?>
                </form>
                <hr>
                <table width="75%" style="font-size: 15; margin-top: 50" border=1>
                    <thead>
                        <tr>
                            <th style="width: 5%"><strong>ID</strong></th>
                            <th style="width: 45%"><strong>Service Name</strong></th>
                            <th style="width: 8%"><strong>Service Price</strong></th>
                            <th style="width: 8%"><strong>Service Point</strong></th>
                            <th style="width: 8%"><strong>Add</strong></th>
                            <th style="width: 8%"><strong>Delete</strong></th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        $count = 1;
                        $sel_query = "SELECT * FROM room;";
                        $result = mysqli_query($baglanti, $sel_query);

                        $room_service_query = "SELECT e.id, e.service, e.service_point, e.service_price, e.hotel_id
                                        FROM extraservice e WHERE e.hotel_id = $row_room[hotel_id]";
                        $result_services = mysqli_query($baglanti, $room_service_query);

                        while ($row_services = mysqli_fetch_array($result_services)) {
                        ?>
                            <tr>
                                <td align="center"><?php echo $count; ?></td>
                                <td align="center"><?php echo $row_services["service"] ?></td>
                                <td align="center"><?php echo $row_services["service_price"], " $" ?></td>
                                <td align="center"><?php echo $row_services["service_point"] ?></td>

                                <td align="center">
                                    <form method="post">
                                        <input type="submit" style="width:100px" name="add" value="Add" /></form>
                                </td>
                                <td align="center">
                                    <form method="post">
                                        <input type="submit" style="width:100px" name="delete" value="Delete" /></form>
                                </td>
                            </tr>
                        <?php $count++;
                        } ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>

</html>