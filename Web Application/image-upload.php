<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase.js"> </script>
<script type="text/javascript">
    var config = {
        apiKey: "AIzaSyBPvVIQ12PN6hWW_eE-5D3FaViinPVfbjQ",
        authDomain: "pet-adomption.firebaseapp.com",
        databaseURL: "https://pet-adomption.firebaseio.com",
        projectId: "pet-adomption",
        storageBucket: "pet-adomption.appspot.com",
        messagingSenderId: "640709970982",
        appId: "1:640709970982:web:483fae29d6df77bfce2ae7",
        measurementId: "G-BGEJRHMQZE"
    };
    firebase.initializeApp(config);
    var selectedFile;

    function getfile() {
        var pic = document.getElementById("photo");

        // selected file is that file which user chosen by html form 
        selectedFile = pic.files[0];

        // make save button disabled for few seconds that has id='submit_link' 
        document.getElementById('submit_link').setAttribute('disabled', 'true');
        myfunction(); // call below written function 
    }

    function myfunction() {
        // select unique name for everytime when image uploaded 
        // Date.now() is function that give current timestamp 
        var name = "123" + Date.now();

        // make ref to your firebase storage and select images folder 
        var storageRef = firebase.storage().ref('/hotel_reservation_images/' + name);

        // put file to firebase  
        var uploadTask = storageRef.put(selectedFile);

        // all working for progress bar that in html 
        // to indicate image uploading... report 
        uploadTask.on('state_changed', function(snapshot) {
            var progress =
                (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
            var uploader = document.getElementById('uploader');
            uploader.value = progress;
            switch (snapshot.state) {
                case firebase.storage.TaskState.PAUSED:
                    console.log('Upload is paused');
                    break;
                case firebase.storage.TaskState.RUNNING:
                    console.log('Upload is running');
                    break;
            }
        }, function(error) {
            console.log(error);
        }, function() {

            // get the uploaded image url back 
            uploadTask.snapshot.ref.getDownloadURL().then(
                function(downloadURL) {

                    document.getElementById('submit_link').removeAttribute('disabled');
                });
        });
    };
</script>

<!doctype html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/style.css" />
</head>

<body>

    <form>
        <p>Resim Yüklenirken Kayıt Butonu 1-2 Saniye Devre Dışı Kalmaktadır.</p>
        <input id="photo" class="file" type="file" name="userfile" value="" onchange="getfile()">
        <button id="submit_link" type="submit" name="button">Save</button>
        </input>
    </form>
</body>

</html>