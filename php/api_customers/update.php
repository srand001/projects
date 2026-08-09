<?php

// API Interface for 'PUT' ie update

require_once 'functions.php';

error_reporting(0); // Disable error messages

header('Access-Control-Allow-Method: PUT');
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Request-With');

$requestMethod = $_SERVER["REQUEST_METHOD"];

include('function.php');

if ($requestMethod == "PUT") {
  $inputData = json_decode(file_get_contents("php://input"), true);
  $updateCustomer = updateCustomer($inputData, $_GET);  // Raw data
  echo $updateCustomer;

  // Note: Form data is not used when using PUT.
  // $customer = updateCustomer($_POST, $_GET);      // Form data

} else {
  $data = [
    'status' => 405,
    'message' => $requestMethod . " Method Not Allowed",
  ];

  header("HTTP/1.0 405 Method Not Allowed");
  echo json_encode($data);
}


?>