

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Image Page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1", charset="utf-8">
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>

<body>

	<?php
    session_start();
    include("navbar3.php");
    ?>
	
	<div class="w3-cell-row" style="margin: 50px">
        <div class="w3-container w3-red w3-cell" style="width: 25%; background: linear-gradient(to right, #6190e8, #a7bfe8);">
            <h2 style="width:80%; margin: auto; margin-top: 50">İmage Upload</h2>
        </div>
        <div class="w3-container">     
		    <h3 style="width:100%; margin: auto; margin-top: 50">Sorry, only JPG, JPEG, PNG & GIF files are allowed.</h3>
           
		<?php
		$target_dir = "C:\AppServ\www\css\image\img-";
		$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
		$uploadOk = 1;
		$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
		// Check if image file is a actual image or fake image
		if (isset($_POST["submit"])) {
			$check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
			if ($check !== false) {
				echo "File is an image - " . $check["mime"] . ".";
				$uploadOk = 1;
			} else {
				echo "File is not an image.";
				$uploadOk = 0;
			}
		}
		// Check if file already exists
		if (file_exists($target_file)) {
			echo "Sorry, file already exists.";
			$uploadOk = 0;
		}
		// Check file size
		if ($_FILES["fileToUpload"]["size"] > 500000) {
			echo "Sorry, your file is too large.";
			$uploadOk = 0;
		}
		// Allow certain file formats
		if (
			$imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
			&& $imageFileType != "gif"
		) {
			$uploadOk = 0;
		}
		// Check if $uploadOk is set to 0 by an error
		if ($uploadOk == 0) {
			// if everything is ok, try to upload file
		} else {
			if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
				echo "The file " . basename($_FILES["fileToUpload"]["name"]) . " has been uploaded.";
			} else {
				echo "Sorry, there was an error uploading your file.";
			}
		}
		?>

		<form method="post" enctype="multipart/form-data">
			Select image to upload:
			<input type="file" name="fileToUpload" id="fileToUpload">
			<input type="submit" name="upload" id="upload" value="Upload Image">
		</form>
		
		</div>
    </div>

</body>

</html>