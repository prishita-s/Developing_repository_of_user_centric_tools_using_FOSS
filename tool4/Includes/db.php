<?php 

        $con = mysqli_connect("localhost","root","","data_crop_buy");
      
        if (mysqli_connect_errno()) {
                echo "Failed to connect to MySql " . mysqli_connect_error();
        }
