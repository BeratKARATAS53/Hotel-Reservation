<html>

<head>
    <meta charset="utf-8">
    <title>Member Page</title>
    <link rel="stylesheet" href="css/style.css" />
    <link rel="stylesheet" href="css/navbar.css" />
    <style>
        table {
            border-collapse: collapse;
        }

        th,
        td {
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2
        }

        th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>

<body>
    <?php
    session_start();
    $email = $_SESSION['email'];
    include('navbar-customer.php');
    $sql = "SELECT * FROM customer_view WHERE email='$email'";
    $result = mysqli_query($baglanti, $sql);
    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
    $id = $row["id"];

    ?>

    <h1 style="width:85%; margin: auto; margin-top: 50; color:#243b55"><b>My Reservations</b></h1>
    <table width="85%" style="font-size: 15; margin: auto; margin-top: 50" border=1>
        <thead>
            <tr>
                <th style="width: 15%"><strong>Reservation ID</strong></th>
                <th style="width: 8%"><strong>Room Number</strong></th>
                <th style="width: 8%"><strong>Price</strong></th>
                <th style="width: 25%"><strong>Hotel Name</strong></th>
                <th style="width: 50%"><strong>Hotel Address</strong></th>
                <th style="width: 8%"><strong>Hotel Telephone</strong></th>
            </tr>
        </thead>
        <tbody>
            <?php
            $sql = "SELECT * FROM customer_reservation cr, room_reservation rr, room r, hotel h 
                    WHERE cr.reservation_id = rr.reservation_id AND rr.room_id = r.id AND r.hotel_id = h.id AND cr.customer_id = $id";
            $result = mysqli_query($baglanti, $sql);
            while ($data = mysqli_fetch_assoc($result)) {
            ?>
                <tr>
                    <td align="center"><?php echo $data["reservation_id"] ?></td>
                    <td align="center"><?php echo $data["room_number"] ?></td>
                    <td align="center"><?php echo $data["price"] . " $" ?></td>
                    <td align="center"><?php echo $data["name"] ?></td>
                    <td align="center"><?php echo $data["address"] ?></td>
                    <td align="center"><?php echo $data["telephone"] ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>


</body>

</html>