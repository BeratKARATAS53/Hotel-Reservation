<?php
require('db.php');
?>
<html>
<title>Hotels</title>
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
            <h2 style="width:80%; margin: auto; margin-top: 50">Hotels</h2>
            <?php
            $search_value = $_POST["search"];
            if ($search_value != '') {
                $sel_query = "SELECT * FROM hotel USE INDEX (hotel_search_index) WHERE name LIKE '%$search_value%' ORDER BY id desc";
            } else {
                $sel_query = "SELECT * FROM hotel ORDER BY id desc";
            }
            $result = mysqli_query($baglanti, $sel_query);
            while ($row = mysqli_fetch_assoc($result)) { ?>
                <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                    <header class="w3-container w3-light-grey">
                        <h4> <?php echo $row["name"] ?> </h4>
                    </header>
                    <p><?php echo "Address: ", $row["address"], " $" . "<br/>",
                            "Phone Number: ",
                            $row["telephone"] . "<br/>",
                            "Stars: ",
                            $row["star"] . "<br/>",
                            "Hotel Type: ",
                            $row["hotel_type"] . "<br/>",
                            "Hotel Info: ",
                            $row["info"] . "<br/>"
                        ?></p>
                    <hr>
                    <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="room-detail.php?id=<?php echo $row["id"]; ?>"> Details </a>
                    <hr style="border: 1px solid black;">
                </div>
                <br />
            <?php  }
            ?>

        </div>
    </div>
</body>

</html>