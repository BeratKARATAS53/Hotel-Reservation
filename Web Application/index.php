<html>

<head>
   <meta charset="utf-8">
   <title>Hotel Reservation</title>
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
   include('navbar.php');
   include('date.php'); ?>

   <table width="80%" style="font-size: 15; margin: auto; margin-top: 50" border=1>
      <thead>
         <tr>
            <th style="width: 5%"><strong>ID</strong></th>
            <th style="width: 45%"><strong>Room Info</strong></th>
            <th style="width: 8%"><strong>Room No</strong></th>
            <th style="width: 8%"><strong>Price</strong></th>
            <th style="width: 8%"><strong>Status</strong></th>
            <th style="width: 8%"><strong>Capacity</strong></th>
            <th style="width: 10%"><strong>Hotel Name</strong></th>
            <th style="width: 18%"><strong>Details</strong></th>
         </tr>
      </thead>
      <tbody>
         <?php
         $count = 1;
         $search_value = $_POST["search"];
         $sel_query = "SELECT * FROM room ORDER BY id desc";
         $result = mysqli_query($baglanti, $sel_query);
         while ($row = mysqli_fetch_assoc($result)) {
            $hotelId = $row['hotel_id'];
            $sel_query2 = "SELECT * FROM hotel WHERE id = $hotelId";
            $result2 = mysqli_query($baglanti, $sel_query2);
            $hotelName = mysqli_fetch_assoc($result2)
         ?>
            <tr>
               <td align="center"><?php echo $count; ?></td>
               <td align="center"><?php echo $row["room_info"]; ?></td>
               <td align="center"><?php echo $row["room_number"]; ?></td>
               <td align="center"><?php echo $row["room_price"], " $" ?></td>
               <td align="center"><?php echo $row["status"]; ?></td>
               <td align="center"><?php echo $row["capacity"]; ?></td>
               <td align="center"><?php echo $hotelName["name"]; ?></td>

               <td align="center">
                  <a href="room-detail.php?id=<?php echo $row["id"]; ?>">Detail</a>
               </td>
            </tr>
         <?php $count++;
         } ?>
      </tbody>
   </table>


</body>

</html>