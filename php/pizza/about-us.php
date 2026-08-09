<?php
session_start();
include_once('includes/dbconnection.php');
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="" />
  <meta name="keywords" content="" />

  <title>About us</title>

  <link rel="stylesheet" href="assets/css/icons.min.css">
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/css/main.css">
  <link rel="stylesheet" href="assets/css/red-color.css">
  <link rel="stylesheet" href="assets/css/yellow-color.css">
  <link rel="stylesheet" href="assets/css/responsive.css">
</head>

<body itemscope>

  <?php include_once('includes/header.php'); ?>
  <section>
    <div class="block">
      <div class="fixed-bg" style="background-image: url(assets/images/topbg.jpg);"></div>
      <div class="page-title-wrapper text-center">
        <div class="col-md-12 col-sm-12 col-lg-12">
          <div class="page-title-inner">
            <h1 itemprop="headline">About Us</h1>
            <br>
            <span>Freshly prepared and delicious cuisine</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="block less-spacing gray-bg top-padd30">
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-sm-12 col-lg-12">
            <div class="sec-box">
              <div class="about-feat text-center wow fadeIn" data-wow-delay="0.2s">
                <h2 class="title3" itemprop="headline">We cater to every taste </h2>
              </div>


              <div class="title1-wrapper text-center style2">
                <div class="title1-inner">
                  Be transported to the beautiful country of Italy with our traditional dishes. From mains such as
                  pizza, pasta and risotto to desserts like tiramisu.
                  Italy is a treasure trove of culinary techniques. From gentle simmering to wood-fired baking, pasta
                  rolling to risotto stirring, it’s all about precision and patience. The regions have developed their
                  own exceptional identities, with the north known for exquisite pasta and the south boasting phenomenal
                  olive oils. Above all else, Italian food celebrates simplicity, using seasonal ingredients with care,
                  love and respect with plenty of olive oil, garlic, tomatoes, wine and herbs playing starring roles
                  across most dishes.
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </section>



  <?php include_once('includes/footer.php');
  include_once('includes/signin.php');
  include_once('includes/signup.php');
  ?>

  </main><!-- Main Wrapper -->

  <script src="assets/js/jquery.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>
  <script src="assets/js/plugins.js"></script>
  <script src="assets/js/main.js"></script>
</body>

</html>