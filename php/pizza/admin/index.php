<?php

session_start();
//error_reporting(0);

error_reporting(E_ALL);
echo "In admin/index.php";

include('includes/dbconnection.php');


if (isset($_POST['login'])) {
  $adminuser = "admin";
  $password = "123";

  //$con = mysqli_connect("localhost", "mintsyst_admin", "mintsyst_pass123xyz", "mintsyst_pizza");
  $sql = "SELECT id FROM tbladmin WHERE UserName='$adminuser' && Password=$password";
  $query = mysqli_query($con, $sql);
  $ret = mysqli_fetch_array($query);

  header('location:dashboard.php');

  if ($ret > 0) {
    $_SESSION['fosaid'] = $ret['id'];
    header('location:dashboard.php');
  } else {
    echo "Invalid login details";
    $msg = "Invalid Details.";
  }
}
?>

<!DOCTYPE html>
<html>

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Admin Login</title> <!-- Was 'zz| Admin' - Surj 25May2026 -->

  <link href="css/bootstrap.min.css" rel="stylesheet">
  <link href="font-awesome/css/font-awesome.css" rel="stylesheet">

  <link href="css/animate.css" rel="stylesheet">
  <link href="css/style.css" rel="stylesheet">

</head>

<!-- Admin login for administrator access level -->

<body class="gray-bg">

  <div class="loginColumns animated fadeInDown">
    <div class="row">

      <!-- Various changes to Admin login - Surj 25May2026 -->

      <div class="col-md-6">
        <h1 class="font-bold" style="color: black;">Admin Login</h1>
        <p style="color: black; font-size: 14px">For demo purposes, the admin user name and password are already
          filled in. Please press 'Login'. </p>
      </div>
      <div class="col-md-6">
        <div class="ibox-content">

          <form class="m-t" role="form" action="" method="post" name="login">
            <div class="form-group">
              <input type="text" class="form-control" style="color: black;" placeholder="username" name="username"
                required="" value="admin">
            </div>
            <div class="form-group">
              <input type="password" class="form-control" style="color: black;" placeholder="Password" required=""
                name="password" value="password">
            </div>
            <button type="submit" class="btn btn-primary block full-width m-b" name="login">Login</button>

          </form>

        </div>
      </div>
    </div>
    <hr />

  </div>
</body>

</html>