<?php
// veritabanı bağlantımızı yaptık
include('db.php');
// veritabanı bağlantısı sağlanmaz ise hata verdirdik
if (mysqli_connect_errno()) {
    echo "MySQL bağlantısı başarısız: " . mysqli_connect_error();
}

// Filtreleme Kısmından Gelen Bilgileri Değişkenlere Aktarma.
$maxprice = $_POST['maxprice'];
$city = $_POST['city'];

?>
<!DOCTYPE html>
<html>

<head>
    <title>Organizations</title>
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
                <label>&nbsp;</label>
                <input type="submit" style="width:100%" name="submit" id="submit" value="FILTER">
            </form>
        </div>
        <div class="w3-container">

            <h2 style="width:80%; margin: auto; margin-top: 50">Organizations</h2>
            <?php
            if ($maxprice || $city) {

                $city = trim($city);

                $filter_sql = "SELECT * FROM organization o, hotel h WHERE o.hotel_id = h.id";

                if ($maxprice) {
                    $filter_sql .= " AND o.price < $maxprice";
                }
                if ($city) {
                    $filter_sql .= " AND h.address LIKE '%$city%'";
                }

                $filter_result = mysqli_query($baglanti, $filter_sql);
                while ($filter_row = mysqli_fetch_assoc($filter_result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $filter_row["name"] ?> </h4>
                        </header>
                        <img src="css/image/img-<?php echo $filter_row["image"] ?>" alt="Organization Image" height="200" width="200">
                        <p><?php echo "Organization Information: ", $filter_row["org_info"] . "<br/>",
                                "Organization Price: ",
                                $filter_row["price"],
                                " $" . "<br/>"
                            ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="org-detail.php?id=<?php echo $filter_row["id"]; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
                <?php  }
            } else {
                $search_value = $_POST["search"];
                if ($search_value != '') {
                    $sel_query = "SELECT * FROM organization o USE index (organization_search_index) 
                                    WHERE o.name like '%$search_value%' ORDER BY O.id desc";
                } else {
                    $sel_query = "SELECT * FROM organization ORDER BY id desc";
                }
                $result = mysqli_query($baglanti, $sel_query);
                while ($row = mysqli_fetch_assoc($result)) { ?>
                    <div style="width:80%; font-size: 15; margin: auto; margin-top: 50">
                        <header class="w3-container w3-light-grey">
                            <h4> <?php echo $row["name"] ?> </h4>
                        </header>
                        <img src="css/image/img-<?php echo $row["image"] ?>" alt="Organization Image" height="200" width="200">
                        <p><?php echo "Organization Information: ", $row["org_info"] . "<br/>",
                                "Organization Price: ",
                                $row["price"],
                                " $" . "<br/>"
                            ?></p>
                        <hr>
                        <a class="w3-button w3-block" style="background: linear-gradient(to right, #7bff61, #93f9b9)" href="org-detail.php?id=<?php echo $row["id"]; ?>"> Details </a>
                        <hr style="border: 1px solid black;">
                    </div>
                    <br />
            <?php  }
            } ?>

        </div>
    </div>

</body>

</html>