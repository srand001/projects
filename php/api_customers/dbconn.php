<?php

$dbName = "customers";
$dbHost = "localhost";
$dbUser = "admin";
$dbPass = "pass123xyz";
$conn = mysqli_connect($dbHost, $dbUser, $dbPass, $dbName);

if (!$conn) {
  error_log("Failed to connect to database!", 0);
  die("Something went wrong");
}

?>