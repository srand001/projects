<?php

// API Interface for 'GET' ie read

require_once 'functions.php';

error_reporting(0); // 0=Disable error messages, 1=show errors

//error_reporting(E_ALL); // Report all PHP errors
//ini_set('display_errors', 'On');

header('Access-Control-Allow-Method: GET');
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');
header('Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Request-With');

$requestMethod = $_SERVER["REQUEST_METHOD"];

include('function.php');

if ($requestMethod == "GET") {

  if (isset($_GET['id'])) {
    $customer = getCustomer($_GET);
    echo $customer;
  } else {
    $customerList = getCustomerList();
    echo $customerList;
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