<?php
include('db.php');
$id = $_REQUEST['id'];
$query = "SELECT * from room where id='" . $id . "'";
$result = mysqli_query($baglanti, $query) or die(mysqli_error($baglanti));
$row = mysqli_fetch_assoc($result);
?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Room Detail</title>
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>
    <div class="form">
        <p><a href="dashboard.php">Dashboard</a>
            | <a href="insert.php">Insert New Record</a>
            | <a href="logout.php">Logout</a></p>
        <h1><?php echo $row["room_number"] ?></h1>
    </div>
</body>

</html>