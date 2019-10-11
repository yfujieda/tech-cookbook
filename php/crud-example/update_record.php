<?php
/*********** 
This is an example of updating a record using PHP and MySQL

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

$sql = "UPDATE test_db.cars SET car_model = 'accord', car_brand = 'honda' WHERE id = '3'";

if(mysqli_query($sql_connection, $sql)){
    echo "Record updated successfully<br>";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($sql_connection);    
}

?>