<!doctype html>
<html>

<body>
    <div style="display: flex; justify-content: center;">
        <h1>Reservation </h1>
        <form action="rooms.php" method="post">
            <br>
            <br>
            <br>
            City:
            <input type="text" style="width:150px" name="city" id="city" placeholder="Ankara">
            Start Date:
            <input type="date" name="start" id="startDate" min='<?php echo date("Y-m-d") ?>'>
            Finish Date:
            <input type="date" name="finish" id="finishDate" min='<?php echo date("Y-m-d") ?>'>
            <input type="submit" id="submit" value="SEARCH">
        </form>
    </div>
</body>

</html>