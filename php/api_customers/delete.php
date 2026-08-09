<?php

// API Interface for 'DELETE' ie delete

require_once 'functions.php';

error_reporting(0); // Disable error messages

header('Access-Control-Allow-Method: DELETE');
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Request-With');

$requestMethod = $_SERVER["REQUEST_METHOD"];

include('function.php');

if ($requestMethod == "DELETE") {

  if (isset($_GET['id'])) {
    $customer = deleteCustomer($_GET);
    echo $customer;
  }

} else {
  $data = [
    'status' => 405,
    'message' => $requestMethod . " Method Not Allowed",
  ];

  header("HTTP/1.0 405 Method Not Allowed");
  echo json_encode($data);
}


?>