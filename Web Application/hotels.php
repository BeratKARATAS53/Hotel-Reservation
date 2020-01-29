<?php
// veritabanı bağlantımızı yaptık
include('db.php');
// veritabanı bağlantısı sağlanmaz ise hata verdirdik
if (mysqli_connect_errno()) {
    echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}

$search_value = $_POST["search"];

// Filtreleme Kısmından Gelen Bilgileri Değişkenlere Aktarma.
$city = $_POST['city'];
$stars = $_POST['stars'];
$type = $_POST['type'];

$city = trim($city);
?>
<!DOCTYPE html>
<html>

<head>
    <title>Hotels</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>

<body>
    <?php
    session_start();
    include("navbar.php");
    ?>

    <div class="w3-cell-row" style="margin: 50px">
        <div class="w3-container w3-red w3-cell" style="width: 25%; background: linear-gradient(to right, #6190e8, #a7bfe8);">
            <h2 style="width:80%; margin-top: 50; color:#243b55"><b>Filters</b></h2>
            <br>
            <form method="post">
                <h4><b>City</b></h4><input type="text" style="width:100%" name="city" id="city" placeholder="Ankara" />
                <hr>
                <h4><b>Stars</b></h4>
                <input type="number" style="width:35%" name="stars" id="stars" min="1" max="10" placeholder="5" />
                <hr>
                <h4><b>Hotel Type</b></h4>
                <p>
                    <?php
                    $sel_query = "SELECT DISTINCT hotel_type FROM hotel ORDER BY hotel_type desc";
                    $result = mysqli_query($baglanti, $sel_query);
                    while ($row = mysqli_fetch_assoc($result)) { ?>
                        <label class="newContainer"><?php echo $row["hotel_type"] ?>
                            <input type="radio" name="type" id="<?php echo $row["hotel_type"] ?>" value="<?php echo $row["hotel_type"] ?>">
                            <span class="newCheckmark"></span>
                        </label>
                    <?php } ?>
                </p>
                <label>&nbsp;</label>
                <input type="submit" style="width:100%" name="submit" id="submit" value="FILTER">
            </form>
        </div>
        <div class="w3-container">
            <h2 style="width:80%; margin: auto; margin-top: 50">Hotels</h2>
            <?php
            if ($city || $stars || $type) {

                $filter_sql = "SELECT * FROM hotel h WHERE h.star < 20";

                if ($city) {
                    $filter_sql .= " AND h.address LIKE '%$city%'";
                }
                if ($stars) {
                    $filter_sql .= " AND h.star = $stars";
                }
                if ($type) {
                    $filter_sql .= " AND h.hotel_type = '$type'";
                }

                $filter_result = mysqli_query($baglanti, $filter_sql);
                while ($filter_row = mysqli_fetch_assoc($filter_result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $filter_row["name"] ?> </h4>
                        </header>
                        <p><?php echo "Address: ", $filter_row["address"], " $" . "<br/>",
                                "Stars: ",
                                $filter_row["star"] . "<br/>",
                                "Hotel Type: ",
                                $filter_row["hotel_type"] . "<br/>"
                            ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="hotel-detail.php?id=<?php echo $filter_row["id"]; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
                <?php  }
            } else if ($search_value) {
                $sel_query2 = "SELECT * FROM hotel USE INDEX (hotel_search_index) WHERE name LIKE '%$search_value%' ORDER BY id desc";
            } else {
                $sel_query2 = "SELECT * FROM hotel ORDER BY id desc";
            }
            $result2 = mysqli_query($baglanti, $sel_query2);
            while ($row2 = mysqli_fetch_assoc($result2)) { ?>
                <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                    <header class="w3-container w3-light-grey">
                        <h4> <?php echo $row2["name"] ?> </h4>
                    </header>
                    <p><?php echo "Address: ", $row2["address"], " $" . "<br/>",
                            "Stars: ",
                            $row2["star"] . "<br/>",
                            "Hotel Type: ",
                            $row2["hotel_type"] . "<br/>"
                        ?></p>
                    <hr>
                    <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="hotel-detail.php?id=<?php echo $row2["id"]; ?>"> Details </a>
                    <hr style="border: 1px solid black;">
                </div>
                <br />
            <?php  }
            ?>

        </div>
    </div>
</body>

</html>