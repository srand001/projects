<?php
// Designed by Surjit Randhawa 2026
// Uses PHP and JavaScript to play checkers game online
// Entry point — checkers board and links assets.
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="Description" content="Play Checkers online against the computer" />

  <!--Open Graph Protocol metadata-->
  <meta property="og:title" content="Checkers" />
  <meta property="og:description" content="Play Checkers online against the computer" />
  <meta property="og:type" content="game" />

  <title>Checkers</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>

  <div class="game-wrapper">
    <h1>Checkers</h1>

    <div class="game-area">
      <div id="board" class="board"></div>

      <div class="panel">
        <div class="panel-section">
          <label for="difficulty">Difficulty</label>
          <select id="difficulty">
            <option value="easy">Easy</option>
            <option value="medium" selected>Medium</option>
            <option value="hard">Hard</option>
          </select>
        </div>

        <div class="panel-section">
          <button id="newGameBtn">New Game</button>
        </div>

        <div class="panel-section status-box">
          <p id="status">Your move (Red)</p>
        </div>

        <div class="panel-section score-box">
          <div class="score red-score">
            <span class="dot red"></span> Red: <span id="redCount">12</span>
          </div>
          <div class="score black-score">
            <span class="dot black"></span> Black: <span id="blackCount">12</span>
          </div>
        </div>

        <div class="panel-section rules-box">
          <strong>Rules</strong>
          <ul>
            <li>You play Red, computer plays Black.</li>
            <li>Captures are mandatory when available.</li>
            <li>Multi-jumps must be completed with the same piece.</li>
            <li>Reach the far row to become a King.</li>
          </ul>
        </div>
      </div>
    </div>

    <footer>&copy; <?php echo date("Y"); ?> Checkers. Designed by RandSoft</footer>
  </div>

  <script src="script.js"></script>
</body>

</html>