<?php
require('db.php');
?>
<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<body>
    <h2 style="width:80%; margin: auto; margin-top: 50">Rooms</h2>
    <?php
    $sel_query = "Select * From room ORDER BY id desc;";
    $result = mysqli_query($baglanti, $sel_query);
    while ($row = mysqli_fetch_assoc($result)) { ?>
        <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
            <header class="w3-container w3-light-grey">
                <h4> <?php echo $row["room_info"] ?> </h4>
            </header>
            <div class="w3-container">
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
        </div>
        </div>
    <?php  } ?>

</body>

</html>