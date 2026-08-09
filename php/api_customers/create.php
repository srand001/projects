<?php

// API Interface for 'POST' ie create

require_once 'functions.php';

error_reporting(0); // Disable error messages

header('Access-Control-Allow-Method: POST');
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Request-With');

$requestMethod = $_SERVER["REQUEST_METHOD"];

include('function.php');

if ($requestMethod == "POST") {

  $inputData = json_decode(file_get_contents("php://input"), true); // Note: Set 2nd param to 'true' to use array data rather than class object 

  if (empty($inputData)) {
    $customer = storeCustomer($_POST);      // Form data
  } else {
    $customer = storeCustomer($inputData);  // Raw data
  }

  echo $customer;

} else {
  $data = [
    'status' => 405,
    'message' => $requestMethod . " Method Not Allowed",
  ];

  header("HTTP/1.0 405 Method Not Allowed");
  echo json_encode($data);
}


?>