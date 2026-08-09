<?php

require 'dbconn.php';


function retsponseJson(int $code, string $response)
{
  $data = [
    'status' => $code,
    'message' => $response
  ];
  echo json_encode($data);
}

function error422(string $message)
{
  header("HTTP/1.0 422 Unprocessable Entity");
  retsponseJson(422, $message);
  exit();
}


function updateCustomer($customerInput, $customerParams)
{
  global $conn;

  if (!isset($customerParams['id'])) {
    return error422("Customer id not found in url");
  } elseif ($customerParams['id'] == null) {
    return error422("Enter the customer id");
  }

  $customerId = mysqli_real_escape_string($conn, $customerParams['id']);

  $fname = mysqli_real_escape_string($conn, $customerInput['fname']);
  $lname = mysqli_real_escape_string($conn, $customerInput['lname']);
  $email = mysqli_real_escape_string($conn, $customerInput['email']);
  $phone = mysqli_real_escape_string($conn, $customerInput['phone']);

  if (empty(trim($fname)))
    return error422("Enter first name to proceed");
  elseif (empty(trim($lname)))
    return error422("Enter last name  to proceed");
  elseif (empty(trim($phone)))
    return error422("Enter phone number to proceed");
  elseif (empty(trim($email)))
    return error422("Enter email to proceed");
  else {

    $sql = "UPDATE customerlist SET fname = '$fname', lname = '$lname', email = '$email', phone = '$phone' WHERE id = '$customerId'";

    $result = mysqli_query($conn, $sql);

    if ($result) {
      header("HTTP/1.0 200 Updated");

      $data = [
        'status' => 200,
        'message' => 'Customer Update Successful',
      ];

      return json_encode($data);

    } else {
      header("HTTP/1.0 500 Internal Server Error");
      retsponseJson(500, "Internal Server Error");
    }
  }

} // End updateCustomer()



function storeCustomer($customerInput)
{
  global $conn;

  $fname = mysqli_real_escape_string($conn, $customerInput['fname']);
  $lname = mysqli_real_escape_string($conn, $customerInput['lname']);
  $email = mysqli_real_escape_string($conn, $customerInput['email']);
  $phone = mysqli_real_escape_string($conn, $customerInput['phone']);

  if (empty(trim($fname)))
    return error422("Enter first name to proceed");
  elseif (empty(trim($lname)))
    return error422("Enter last name  to proceed");
  elseif (empty(trim($phone)))
    return error422("Enter phone number to proceed");
  elseif (empty(trim($email)))
    return error422("Enter email to proceed");
  else {

    $result = mysqli_query($conn, "INSERT INTO customerlist (fname, lname,  phone, email) VALUES ('$fname', '$lname', '$phone', '$email')");

    if ($result) {
      header("HTTP/1.0 201 Created");

      $data = [
        'status' => 201,
        'message' => 'Customer Create Successful',
      ];

      return json_encode($data);

    } else {
      header("HTTP/1.0 500 Internal Server Error");
      retsponseJson(500, "Internal Server Error");
    }
  }
} // End storeCustomer()


function getCustomerList()
{
  global $conn;

  $sql = "SELECT * FROM customerlist";

  $result = mysqli_query($conn, $sql);

  if ($result) {

    if (mysqli_num_rows($result) > 0) {

      $res = mysqli_fetch_all($result);

      $data = [
        'status' => 200,
        'message' => 'Get Customer List Successful',
        'data' => $res,
      ];

      header("HTTP:/1.0 200 OK");
      return json_encode($data);

    } else {
      $data = [
        'status' => 404,
        'message' => 'No Customers Found',
      ];

      header("HTTP:/1.0 No Customers Found");
      return json_encode($data);
    }

  } else {

    $data = [
      'status' => 500,
      'message' => 'Internal Server Error',
    ];

    header("HTTP/1.0 500 Internal Server Error");

    return json_encode($data);
  }

} // End getCustomerList()


function getCustomer($customerParams)
{
  global $conn;

  if ($customerParams['id'] == null) {
    $data = [
      'status' => 422,
      'message' => 'Enter valid id',
    ];

    header("HTTP:/1.0 422 Unprocessable Content");
    return json_encode($data); // Error - the index was null
  }

  $id = mysqli_real_escape_string($conn, $customerParams['id']);

  $sql = "SELECT * FROM customerlist WHERE id='$id' LIMIT 1";

  $result = mysqli_query($conn, $sql);

  if ($result) {

    if (mysqli_num_rows($result) == 1) {

      $res = mysqli_fetch_assoc($result);

      $data = [
        'status' => 200,
        'message' => 'Get Customer Successful',
        'data' => $res,
      ];

      header("HTTP:/1.0 200 OK");
      return json_encode($data);

    } else {
      $data = [
        'status' => 404,
        'message' => 'No Customer Found',
      ];

      header("HTTP:/1.0 No Customer Found");
      return json_encode($data);
    }

  } else {

    $data = [
      'status' => 500,
      'message' => 'Internal Server Error',
    ];

    header("HTTP/1.0 500 Internal Server Error");

    return json_encode($data);
  }

} // End getCustomer()


function deleteCustomer($customerParams)
{
  global $conn;

  if ($customerParams['id'] == null) {
    $data = [
      'status' => 422,
      'message' => 'Enter valid id',
    ];

    header("HTTP:/1.0 422 Unprocessable Content");
    return json_encode($data); // Error - the index was null
  }

  $id = mysqli_real_escape_string($conn, $customerParams['id']);

  $sql = "DELETE FROM customerlist WHERE id='$id' LIMIT 1";

  $result = mysqli_query($conn, $sql);

  if ($result) {

    $res = mysqli_fetch_assoc($result);

    $data = [
      'status' => 204,
      'message' => 'Delete Customer Successful',
    ];

    header("HTTP:/1.0 204 OK");
    return json_encode($data);

  } else {
    $data = [
      'status' => 404,
      'message' => 'No Customer Found',
    ];

    header("HTTP:/1.0 No Customer Found");
    return json_encode($data);
  }
} // End deleteCustomer()

?>