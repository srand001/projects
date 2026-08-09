<?php
	session_start();
	require 'dbconn.php';
?>

<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

  <title>Book Edit</title>
</head>

<body>

  <div class="container mt-5">

    <?php include('message.php'); ?>

    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h4>Book Edit
              <a href="index.php" class="btn btn-danger float-end">BACK</a>
            </h4>
          </div>
          <div class="card-body">

            <?php
            if (isset($_GET['id'])) {
              $book_id = mysqli_real_escape_string($con, $_GET['id']);
              $query = "SELECT * FROM booklist WHERE id='$book_id' ";
              $query_run = mysqli_query($con, $query);

              if (mysqli_num_rows($query_run) > 0) {
                $book = mysqli_fetch_array($query_run);
                ?>
                <form action="code.php" method="POST">
                  <input type="hidden" name="book_id" value="<?= $book['id']; ?>">

                  <div class="mb-3">
                    <label>Book Title</label>
                    <input type="text" name="title" value="<?= $book['title']; ?>" class="form-control">
                  </div>
                  <div class="mb-3">
                    <label>Author</label>
                    <input type="text" name="author" value="<?= $book['author']; ?>" class="form-control">
                  </div>
                  <div class="mb-3">
                    <label>Year</label>
                    <input type="text" name="year" value="<?= $book['bookyear']; ?>" class="form-control">
                  </div>
                  <div class="mb-3">
                    <label>Description</label>
                    <input type="text" name="description" value="<?= $book['bookdescription']; ?>" class="form-control">
                  </div>
                  <div class="mb-3">
                    <button type="submit" name="update_book" class="btn btn-primary">
                      Update Book
                    </button>
                  </div>

                </form>
                <?php
              } else {
                echo "<h4>No Such Id Found</h4>";
              }
            }
            ?>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html>