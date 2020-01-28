<?php
require('db.php');
?>
<!DOCTYPE html>
<html>
<title>Rooms</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<body>
    <?php
    include("navbar.php");
    ?>

    <div class="w3-cell-row" style="margin: 50px">
        <div class="w3-container w3-red w3-cell" style="width: 25%; background: linear-gradient(to right, #6190e8, #a7bfe8);">
            <h2 style="width:80%; margin: auto; margin-top: 50">Filters</h2>
        </div>
        <div class="w3-container">

            <h2 style="width:80%; margin: auto; margin-top: 50">Rooms</h2>
            <?php
            if (isset($_POST['city']) && isset($_POST['startDate']) && isset($_POST['finishDate'])) //when form submitted
            {
                $city = $_POST['city'];
                $startDate = $_POST['startDate'];
                $finishDate = $_POST['finishDate'];
                echo $city, $startDate, $finishDate;

                $reserve_sql = "SELECT * FROM room r WHERE r.hotel_id in(SELECT id FROM hotel WHERE address LIKE '%$city%' AND r.id not in(
                    SELECT r2.id FROM reservation r, room_reservation rr, room r2 
                    WHERE r.id=rr.reservation_id AND rr.room_id=r2.id AND r.start_date >= date_format('$startDate', '%Y-%m-%D')
                    AND r.finish_date <= date_format('$finishDate', '%Y-%m-%D')
                    ))";
                $reserve_result = mysqli_query($baglanti, $reserve_sql);
                while ($reserve_row = mysqli_fetch_assoc($reserve_result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $row["room_info"] ?> </h4>
                        </header>
                        <p><?php echo "Room Price: ", $row["room_price"], " $" . "<br/>",
                                "Room Number: ",
                                $row["room_number"] . "<br/>",
                                "Room Status: ",
                                $row["status"] . "<br/>",
                                "Room Capacity: ",
                                $row["capacity"],
                                " Person" . "<br/>" ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="room-detail.php?id=<?php echo $row["id"]; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
                <?php  }
            } else {
                $search_value = $_POST["search"];
                if ($search_value != '') {
                    $sel_query = "SELECT * FROM room USE INDEX (room_search_index) WHERE room_info LIKE '%$search_value%' ORDER BY id desc";
                } else {
                    $sel_query = "SELECT * FROM room ORDER BY id desc";
                }
                $result = mysqli_query($baglanti, $sel_query);
                while ($row = mysqli_fetch_assoc($result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $row["room_info"] ?> </h4>
                        </header>
                        <p><?php echo "Room Price: ", $row["room_price"], " $" . "<br/>",
                                "Room Number: ",
                                $row["room_number"] . "<br/>",
                                "Room Status: ",
                                $row["status"] . "<br/>",
                                "Room Capacity: ",
                                $row["capacity"],
                                " Person" . "<br/>" ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="room-detail.php?id=<?php echo $row["id"]; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
            <?php  }
            } ?>

        </div>
    </div>

</body>

</html>