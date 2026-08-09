<?php

$con = mysqli_connect("localhost", "mintsyst_admin", "mintsyst_pass123xyz", "mintsyst_pizza");  // Database login updated - Surj May2026

if (mysqli_connect_errno()) {
  echo "Connection Fail" . mysqli_connect_error();
}

?>