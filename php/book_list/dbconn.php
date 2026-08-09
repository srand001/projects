<?php
	$dbName = "books";
	$dbHost = "localhost";
	$dbUser = "admin";
	$dbPass = "pass123xyz";
	$con = mysqli_connect($dbHost, $dbUser, $dbPass, $dbName);

	if (!$con) {
		die("Something went wrong");
	}
?>