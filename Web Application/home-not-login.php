</html>

<?php
include('db.php');
?>

<html>

<head>
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

   <meta charset="utf-8">
   <title>Member Page</title>
   <link rel="stylesheet" href="css/style.css" />
   <link rel="stylesheet" href="css/navbar.css" />
</head>

<body>
   <?php
   include("navbar-not-login.php")
   ?>

   <table width="80%" style="font-size: 15; margin: auto; margin-top: 50" border=1>
      <thead>
         <tr>
            <th style="width: 5%"><strong>ID</strong></th>
            <th style="width: 45%"><strong>Room Info</strong></th>
            <th style="width: 8%"><strong>Room No</strong></th>
            <th style="width: 8%"><strong>Price</strong></th>
            <th style="width: 8%"><strong>Status</strong></th>
            <th style="width: 8%"><strong>Capacity</strong></th>
            <th style="width: 10%"><strong>Hotel ID</strong></th>
            <th style="width: 18%"><strong>Details</strong></th>
         </tr>
      </thead>
      <tbody>
         <?php
         $count = 1;
         $sel_query = "Select * From room;";
         $result = mysqli_query($baglanti, $sel_query);
         while ($row = mysqli_fetch_assoc($result)) { ?>
            <tr>
               <td align="center"><?php echo $count; ?></td>
               <td align="center"><?php echo $row["room_info"]; ?></td>
               <td align="center"><?php echo $row["room_number"]; ?></td>
               <td align="center"><?php echo $row["room_price"], " $" ?></td>
               <td align="center"><?php echo $row["status"]; ?></td>
               <td align="center"><?php echo $row["capacity"]; ?></td>
               <td align="center"><?php echo $row["hotel_id"]; ?></td>

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