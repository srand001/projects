<!doctype html>
<html lang="en">

<head>
	<!-- Designed by Surjit Randhawa 2026 -->

  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

  <style>
    h1 {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 50px;
      font-weight: bold;
      /* Apply a black stroke with a width of 3 pixels */
      -webkit-text-stroke-color: black;
      -webkit-text-stroke-width: thin;

      /* Set the text fill color to white */
      color: white;
      text-align: center;
      margin-top: 10px;
    }

    h2 {
      font-size: 30px;

      /* Apply a black stroke with a width of 1 pixels */
      -webkit-text-stroke-color: black;
      -webkit-text-stroke-width: thin;

      /* Set the text fill color to white */
      color: white;
      text-align: center;
      margin-top: 10px;
      margin-bottom: 20px;
    }

    body {
      background-image: url('tfl.png');
      background-size: 100vw 100vh;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-position: center;
      background-size: cover;
    }

    table,
    th,
    tr {
      margin-left: auto;
      margin-right: auto;
      width: 50%;
      border: 1px solid black;
      text-align: center;
      font-size: 25px;
      background-color: white;
    }
  </style>

  <title>TFL Tube Trains</title>
</head>

<body>

  <h1>London Underground</h1>
  <h2>Current Line Status (TFL)</h2>

  <table>

    <?php
    // Define the TfL Tube Status endpoint
    $url = "https://api.tfl.gov.uk/Line/Mode/tube/Status";

    // Optional: Append your API credentials to prevent rate limits
    // $url .= "?app_key=YOUR_API_KEY";

    $DebugMode = 0;  //0=Live using real data, 1=Debug mode using test data

    if ($DebugMode == 0) {
      // Fetch the live JSON data
      $response = file_get_contents($url);

      if ($response === FALSE) {
        die("Error fetching data from TfL API.");
      }
      // Decode the JSON data into a PHP array
      $lines = json_decode($response, true);
    } else {

      $lines[0] = ["name" => "Bakerloo"];
      $lines[1] = ["name" => "Northern"];
      $lines[2] = ["name" => "Central"];
      $lines[3] = ["name" => "Circle"];
    }

    //echo "<tr><th>Line</th><th>Status</th><th>Details</th></tr>";
    echo "<tr><th>Line</th><th>Status</th></tr>";   // No need for line details

    foreach ($lines as $line) {
      $lineName = $line['name'];

      // Extract the primary status description (e.g., "Good Service", "Minor Delays")
      $statusDescription = $line['lineStatuses'][0]['statusSeverityDescription'] ?? 'Unknown';

      // Extract specific reasons/disruption details if available
      $reason = $line['lineStatuses'][0]['reason'] ?? 'No disruptions';

      if ($DebugMode == 1) {
        $statusDescription = "Good Service";
      }

      $bgColor = "white";

      $tableColours = [
        "Bakerloo" => "brown",
        "Central" => "red",
        "Circle" => "yellow",
        "District" => "green",
        "Elizabeth" => "violet",
        "Hammersmith & City" => "pink",
        "Jubilee" => "gray",
        "Metropolitan" => "purple",
        "Northern" => "black",
        "Piccadilly" => "navy",
        "Victoria" => "dodgerblue",
        "Waterloo & City" => "mediumaquamarine",
      ];

      $bgColor = $tableColours[$lineName];
      $textColour = "white";

      if ($lineName == "Circle" || $lineName == "Hammersmith & City") {
        $textColour = "black";
      }

      $tableRowText = "<td style = 'color: $textColour; background-color: $bgColor'> $lineName </td>";

      //<td style="color:white; background-color:brown">Table Cell</td>
      //$tableRowText = "<td style='color:white; background-color:brown'>Table Cell</td>";

      echo "<tr>";
      echo $tableRowText;
      echo "<td>" . htmlspecialchars($statusDescription) . "</td>";
      echo "</tr>";
    } // End: For each loop
    ?>

  </table>