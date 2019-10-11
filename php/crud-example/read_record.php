<?php

/*********** 
This is an example of reading the records using PHP and MySQL

github: https://github.com/yfujieda
twitter: https://twitter.com/yfujieda_
10/11/2019
***********/


// server info
$server_name = "localhost:3306";
$username = "yourusername";
$password = "yourpassword";
$dbname = "test_db";

$sql_connection = new mysqli($server_name, $username, $password, $dbname);

if($sql_connection->connrct_error){
    die("Connection failed: " . $sql_connection->connect_error);
}

$sql = "SELECT * FROM test_db.cars";

$result = $sql_connection->query($sql);

if($result->num_rows > 0){
    while($row = $result->fetch_assoc()){
        
        echo($row["car_model"] . " - " . $row["car_brand"] . "<br>");
    
    }
}

?>