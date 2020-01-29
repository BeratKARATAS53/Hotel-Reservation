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
    include('navbar-employees.php');
    $sql = "SELECT * FROM person WHERE email='$email'";
    $result = mysqli_query($baglanti, $sql);
    $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
    $id = $row["id"];

    $sql2 = "";
    if ($row["p_role"] == "manager") {
        $sql = "SELECT * FROM manager WHERE person_id = $id";
        $result = mysqli_query($baglanti, $sql);
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);

        $hotel_id = $row["hotel_id"];
        $sql2 = "SELECT * FROM manager m, hotel h WHERE m.hotel_id = h.id AND m.hotel_id = $hotel_id";
    } else if ($row["p_role"] == "employee") {
        $sql = "SELECT * FROM employee WHERE person_id = $id";
        $result = mysqli_query($baglanti, $sql);
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);

        $hotel_id = $row["hotel_id"];
        $sql2 = "SELECT * FROM employee e, hotel h WHERE e.hotel_id = h.id AND e.hotel_id = $hotel_id";
    }

    $result2 = mysqli_query($baglanti, $sql2);
    $row2 = mysqli_fetch_array($result2, MYSQLI_ASSOC);

    $hotel_id = $row2["hotel_id"];

    ?>

    <table width="50%" style="font-size: 15; margin: auto; margin-top: 50" border=1>
        <thead>
            <tr>
                <th style="width: 15%"><strong>Operation</strong></th>
                <th style="width: 45%"><strong>Information</strong></th>
                <th style="width: 8%"><strong>Result</strong></th>
            </tr>
        </thead>
        <tbody>
            <?php
            $sql = "SELECT COUNT(id) as total FROM room WHERE hotel_id = $hotel_id";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">COUNT</td>
                <td align="center">Number of Rooms in The Hotel</td>
                <td align="center"><?php echo $data["total"] ?></td>
            </tr>
            <?php
            $sql = "SELECT COUNT(id) as total FROM room WHERE hotel_id = $hotel_id AND status = 'available'";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">COUNT</td>
                <td align="center">Number of Available Rooms in The Hotel</td>
                <td align="center"><?php echo $data["total"] ?></td>
            </tr>
            <?php
            $sql = "SELECT COUNT(id) as total FROM room WHERE hotel_id = $hotel_id AND status = 'not available'";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">COUNT</td>
                <td align="center">Number of Not Available Rooms in The Hotel</td>
                <td align="center"><?php echo $data["total"] ?></td>
            </tr>
            <?php
            $sql = "SELECT COUNT(id) as total FROM room_reservation rr, room r WHERE rr.room_id = r.id AND r.hotel_id = $hotel_id";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">COUNT</td>
                <td align="center">Number of Reserved Rooms in The Hotel</td>
                <td align="center"><?php echo $data["total"] ?></td>
            </tr>
            <?php
            $sql = "SELECT MAX(room_price) as maxprice FROM room r WHERE r.hotel_id = $hotel_id";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">MAX</td>
                <td align="center">Maximum Price of Rooms in The Hotel</td>
                <td align="center"><?php echo $data["maxprice"] . " $" ?></td>
            </tr>
            <?php
            $sql = "SELECT MIN(room_price) as minprice FROM room r WHERE r.hotel_id = $hotel_id";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">MIN</td>
                <td align="center">Minimum Price of Rooms in The Hotel</td>
                <td align="center"><?php echo $data["minprice"] . " $" ?></td>
            </tr>
            <?php
            $sql = "SELECT AVG(room_price) as avgprice FROM room r WHERE r.hotel_id = $hotel_id";
            $result = mysqli_query($baglanti, $sql);
            $data = mysqli_fetch_assoc($result);
            ?>
            <tr>
                <td align="center">AVG</td>
                <td align="center">Average Price of Rooms in The Hotel</td>
                <td align="center"><?php echo $data["avgprice"] . " $" ?></td>
            </tr>
        </tbody>
    </table>


</body>

</html>
<script>
    $(document).ready(function() {
        $('#create_excel').click(function() {
            <?php

            require dirname(__FILE__) . '/php-excel.class.php';

            $xls = new Excel_XML;
            $xls->sendWorkbook('report.xml');

            ?>
        });
    });
</script>