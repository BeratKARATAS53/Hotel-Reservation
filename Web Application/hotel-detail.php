<?php
require('db.php');
?>

<!DOCTYPE html>
<html>

<head>
    <title>Hotel Detail</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <?php
    session_start();
    include("navbar.php");

    $id = $_GET['id'];

    $hotel_query = "SELECT * FROM hotel WHERE id = $id ORDER BY id desc";
    $result_hotel = mysqli_query($baglanti, $hotel_query);

    $row_hotel = mysqli_fetch_array($result_hotel, MYSQLI_ASSOC);
    $hotel_id = $row_hotel["id"];

    ?>

    <div class="w3-cell-row" style="margin: 50px">
        <div class="w3-container">
            <div style="width:100%; font-size: 15; margin: auto; margin-top: 50">
                <header class="w3-container w3-light-grey">
                    <h4> <?php echo $row_hotel["name"] ?> </h4>
                </header>
                <div class="w3-container">
                    <p>
                        <?php echo
                            "Hotel Info: ",
                            $row_hotel["hotel_info"] . "<br/>",
                            "Address: ",
                            $row_hotel["address"],
                            " $" . "<br/>",
                            "Phone Number: ",
                            $row_hotel["telephone"] . "<br/>",
                            "Stars: ",
                            $row_hotel["star"] . "<br/>",
                            "Hotel Type: ",
                            $row_hotel["hotel_type"] . "<br/>"
                        ?>
                    </p>
                </div>
                <br><br>
                <hr>
                <table width="80%" style="font-size: 15; margin: auto; margin-top: 50" border=1>
                    <thead>
                        <tr>
                            <th style="width: 5%"><strong>ID</strong></th>
                            <th style="width: 45%"><strong>Room Info</strong></th>
                            <th style="width: 8%"><strong>Room No</strong></th>
                            <th style="width: 8%"><strong>Price</strong></th>
                            <th style="width: 8%"><strong>Status</strong></th>
                            <th style="width: 8%"><strong>Capacity</strong></th>
                            <th style="width: 18%"><strong>Details</strong></th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        $count = 1;
                        $search_value = $_POST["search"];
                        $sel_query = "SELECT * FROM room WHERE hotel_id = $hotel_id ORDER BY id desc";
                        $result = mysqli_query($baglanti, $sel_query);
                        while ($row = mysqli_fetch_assoc($result)) {
                            $hotelId = $row['hotel_id'];
                            $sel_query2 = "SELECT * FROM hotel WHERE id = $hotelId";
                            $result2 = mysqli_query($baglanti, $sel_query2);
                            $hotelName = mysqli_fetch_assoc($result2)
                        ?>
                            <tr>
                                <td align="center"><?php echo $count; ?></td>
                                <td align="center"><?php echo $row["room_info"]; ?></td>
                                <td align="center"><?php echo $row["room_number"]; ?></td>
                                <td align="center"><?php echo $row["room_price"], " $" ?></td>
                                <td align="center"><?php echo $row["status"]; ?></td>
                                <td align="center"><?php echo $row["capacity"]; ?></td>

                                <td align="center">
                                    <a href="room-detail.php?id=<?php echo $row["id"]; ?>">Detail</a>
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