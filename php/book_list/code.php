<?php
	session_start();
	require 'dbconn.php';

	if (isset($_POST['delete_book'])) {
		$book_id = mysqli_real_escape_string($con, $_POST['delete_book']);

		$query = "DELETE FROM booklist WHERE id='$book_id' ";
		$query_run = mysqli_query($con, $query);

  if ($query_run) {
    $_SESSION['message'] = "Book Deleted Successfully";
    header("Location: index.php");
    exit(0);
  } else {
    $_SESSION['message'] = "Book Not Deleted";
    header("Location: index.php");
    exit(0);
  }
}

if (isset($_POST['update_book'])) {
  $book_id = mysqli_real_escape_string($con, $_POST['book_id']);

  $title = mysqli_real_escape_string($con, $_POST['title']);
  $author = mysqli_real_escape_string($con, $_POST['author']);
  $year = mysqli_real_escape_string($con, $_POST['year']);
  $description = mysqli_real_escape_string($con, $_POST['description']);

  $query = "UPDATE booklist SET title='$title', author='$author', bookyear='$year', bookdescription='$description' WHERE id='$book_id' ";
  $query_run = mysqli_query($con, $query);

  if ($query_run) {
    $_SESSION['message'] = "Book Updated Successfully";
    header("Location: index.php");
    exit(0);
  } else {
    $_SESSION['message'] = "Book Not Updated";
    header("Location: index.php");
    exit(0);
  }
}

if (isset($_POST['save_book'])) {
  $author = mysqli_real_escape_string($con, $_POST['author']);
  $title = mysqli_real_escape_string($con, $_POST['title']);
  $year = mysqli_real_escape_string($con, $_POST['year']);
  $description = mysqli_real_escape_string($con, $_POST['description']);

  $query = "INSERT INTO booklist (author,title,bookyear,bookdescription) VALUES ('$author','$title','$year','$description')";

  $query_run = mysqli_query($con, $query);
  if ($query_run) {
    $_SESSION['message'] = "Book Created Successfully";
    header("Location: book-add.php");
    exit(0);
  } else {
    $_SESSION['message'] = "Book Not Created";
    header("Location: book-add.php");
    exit(0);
  }
}

?>