<?php
// veritabanı bağlantımızı yaptık
include('db.php');
// veritabanı bağlantısı sağlanmaz ise hata verdirdik
if (mysqli_connect_errno()) {
    echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}

// Reservasyon Kısmından Gelen Bilgileri Değişkenlere Aktarma.
$city = $_POST['city'];
$startDate = $_POST['start'];
$finishDate = $_POST['finish'];

// Filtreleme Kısmından Gelen Bilgileri Değişkenlere Aktarma.
$maxprice = $_POST['maxprice'];
$city = $_POST['city'];
$capacity = $_POST['capacity'];
$status = $_POST['status'];

$city = trim($city);
?>
<!DOCTYPE html>
<html>

<head>
    <title>Rooms</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>

<body>
    <?php
    session_start();
    include("navbar.php");
    ?>

    <div class="w3-cell-row" style="margin: 50px">
        <div class="w3-container w3-red w3-cell" style="width: 25%; background: linear-gradient(to right, #6190e8, #a7bfe8); max-height: 150px">
            <h2 style="width:80%; margin-top: 50; color:#243b55"><b>Filters</b></h2>
            <br>
            <form method="post">
                <h4><b>Maximum Price</b></h4>
                <input type="number" style="width:35%" name="maxprice" id="maxprice" min="0" max="100000" placeholder="1000 $" />
                <hr>
                <h4><b>City</b></h4><input type="text" style="width:100%" name="city" id="city" placeholder="Ankara" />
                <hr>
                <hr>
                <h4><b>Capacity</b></h4>
                <input type="number" style="width:35%" name="capacity" id="capacity" min="1" max="10" placeholder="1" />
                <hr>
                <h4><b>Status</b></h4>
                <p>
                    <label class="newContainer">Available
                        <input type="radio" name="status" id="available" value="available">
                        <span class="newCheckmark"></span>
                    </label>
                    <label class="newContainer">Not Available
                        <input type="radio" name="status" id="not_available" value="not available">
                        <span class="newCheckmark"></span>
                    </label>
                </p>
                <label>&nbsp;</label>
                <input type="submit" style="width:100%" name="submit" id="submit" value="FILTER">
            </form>
        </div>
        <div class="w3-container">

            <h2 style="width:80%; margin: auto; margin-top: 50">Rooms</h2>
            <?php
            if ($maxprice || $city || $capacity || $status) {

                $price =  trim($price);
                $city = trim($city);
                $capacity =  trim($capacity);

                $filter_sql = "SELECT * FROM room r, hotel h WHERE r.hotel_id = h.id";

                if ($maxprice) {
                    $filter_sql .= " AND r.room_price < $maxprice";
                }
                if ($city) {
                    $filter_sql .= " AND h.address LIKE '%$city%'";
                }
                if ($capacity) {
                    $filter_sql .= " AND r.capacity <= $capacity";
                }
                if ($status) {
                    $filter_sql .= " AND r.status = '$status'";
                }

                $filter_result = mysqli_query($baglanti, $filter_sql);
                while ($filter_row = mysqli_fetch_assoc($filter_result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $filter_row["room_info"] ?> </h4>
                        </header>
                        <img src="css/image/img-<?php echo $filter_row["image"] ?>" alt="Room Image" height="200" width="200">
                        <p><?php echo "Room Price: ",
                                $filter_row["room_price"],
                                " $" . "<br/>",
                                "Room Number: ",
                                $filter_row["room_number"] . "<br/>",
                                "Room Status: ",
                                $filter_row["status"] . "<br/>",
                                "Room Capacity: ",
                                $filter_row["capacity"],
                                " Person" . "<br/>" ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="room-detail.php?id=<?php echo $filter_row["id"]; ?>&start=<?php echo $startDate; ?>&finish=<?php echo $finishDate; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
                <?php  }
            } else if ($city && $startDate && $finishDate) // when form submitted
            {

                $reserve_sql = "SELECT * FROM room r WHERE r.status = 'available' AND r.hotel_id in(
                    SELECT id FROM hotel WHERE address LIKE '%$city%' AND r.id not in(
                    SELECT r2.id FROM reservation r, room_reservation rr, room r2 
                    WHERE r.id=rr.reservation_id AND rr.room_id=r2.id AND r.start_date >= date_format('$startDate', '%Y-%m-%D')
                    AND r.finish_date <= date_format('$finishDate', '%Y-%m-%D')
                    ))";
                $reserve_result = mysqli_query($baglanti, $reserve_sql);
                while ($reserve_row = mysqli_fetch_assoc($reserve_result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $reserve_row["room_info"] ?> </h4>
                        </header>

                        <img src="css/image/img-<?php echo $reserve_row["image"] ?>" alt="Room Image" height="200" width="200">
                        <p><?php echo "Room Price: ",
                                $reserve_row["room_price"],
                                " $" . "<br/>",
                                "Room Number: ",
                                $reserve_row["room_number"] . "<br/>",
                                "Room Status: ",
                                $reserve_row["status"] . "<br/>",
                                "Room Capacity: ",
                                $reserve_row["capacity"],
                                " Person" . "<br/>" ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="room-detail.php?id=<?php echo $reserve_row["id"]; ?>&start=<?php echo $startDate; ?>&finish=<?php echo $finishDate; ?>"> Details </a>
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
                        <img src="css/image/img-<?php echo $row["image"] ?>" alt="Room Image" height="200" width="200">
                        <p><?php echo "Room Price: ",
                                $row["room_price"],
                                " $" . "<br/>",
                                "Room Number: ",
                                $row["room_number"] . "<br/>",
                                "Room Status: ",
                                $row["status"] . "<br/>",
                                "Room Capacity: ",
                                $row["capacity"],
                                " Person" . "<br/>" ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="room-detail.php?id=<?php echo $row["id"]; ?>&start=<?php echo $startDate; ?>&finish=<?php echo $finishDate; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
            <?php  }
            } ?>

        </div>
    </div>

</body>

</html>