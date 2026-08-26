let board = [];
let turn = 'r';               // 'r' = human (red), 'b' = computer (black)
let selected = null;          // [row, col]
let highlightedMoves = [];    // [{to:[r,c], capture:[r,c]|null}]
let forcedPiece = null;       // piece forced to continue a multi-jump
let mustCaptureSquares = [];  // squares that must move this turn ("r,c" strings)
let difficulty = 'medium';
let gameOver = false;
let thinking = false;

function initBoard() {
  board = Array.from({ length: 8 }, () => Array(8).fill(null));
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 8; c++) {
      if ((r + c) % 2 === 1) board[r][c] = 'b';
    }
  }
  for (let r = 5; r < 8; r++) {
    for (let c = 0; c < 8; c++) {
      if ((r + c) % 2 === 1) board[r][c] = 'r';
    }
  }
  turn = 'r';
  selected = null;
  forcedPiece = null;
  highlightedMoves = [];
  gameOver = false;
  thinking = false;
  updateMustCapture();
  render();
  setStatus('Your move (Red)');
}

function inBounds(r, c) { return r >= 0 && r < 8 && c >= 0 && c < 8; }
function colorOf(v) { return v ? v.toLowerCase() : null; }
function isKing(v) { return v === 'R' || v === 'B'; }
function opp(c) { return c === 'r' ? 'b' : 'r'; }

function forwardDirs(color, king) {
  if (king) return [[-1, -1], [-1, 1], [1, -1], [1, 1]];
  return color === 'r' ? [[-1, -1], [-1, 1]] : [[1, -1], [1, 1]];
}

function getJumpsForPiece(r, c) {
  const v = board[r][c];
  if (!v) return [];
  const color = colorOf(v), king = isKing(v);
  const jumps = [];
  for (const [dr, dc] of forwardDirs(color, king)) {
    const mr = r + dr, mc = c + dc, lr = r + 2 * dr, lc = c + 2 * dc;
    if (!inBounds(lr, lc)) continue;
    const midV = board[mr][mc];
    if (!midV || colorOf(midV) !== opp(color)) continue;
    if (board[lr][lc]) continue;
    jumps.push({ to: [lr, lc], capture: [mr, mc] });
  }
  return jumps;
}

function getSimpleMovesForPiece(r, c) {
  const v = board[r][c];
  if (!v) return [];
  const color = colorOf(v), king = isKing(v);
  const moves = [];
  for (const [dr, dc] of forwardDirs(color, king)) {
    const nr = r + dr, nc = c + dc;
    if (!inBounds(nr, nc)) continue;
    if (!board[nr][nc]) moves.push({ to: [nr, nc], capture: null });
  }
  return moves;
}

function updateMustCapture() {
  mustCaptureSquares = [];
  for (let r = 0; r < 8; r++) {
    for (let c = 0; c < 8; c++) {
      const v = board[r][c];
      if (v && colorOf(v) === turn && getJumpsForPiece(r, c).length > 0) {
        mustCaptureSquares.push(r + ',' + c);
      }
    }
  }
}

function hasAnyMove(color) {
  for (let r = 0; r < 8; r++) {
    for (let c = 0; c < 8; c++) {
      const v = board[r][c];
      if (v && colorOf(v) === color) {
        if (getJumpsForPiece(r, c).length > 0 || getSimpleMovesForPiece(r, c).length > 0) return true;
      }
    }
  }
  return false;
}

function render() {
  const boardEl = document.getElementById('board');
  boardEl.innerHTML = '';
  for (let r = 0; r < 8; r++) {
    for (let c = 0; c < 8; c++) {
      const sq = document.createElement('div');
      sq.className = 'square ' + ((r + c) % 2 === 1 ? 'dark' : 'light');

      const v = board[r][c];
      if (v) {
        const p = document.createElement('div');
        p.className = 'piece ' + (colorOf(v) === 'r' ? 'red' : 'black') + (isKing(v) ? ' king' : '');
        sq.appendChild(p);
      }

      if (selected && selected[0] === r && selected[1] === c) sq.classList.add('selected');

      const hm = highlightedMoves.find(m => m.to[0] === r && m.to[1] === c);
      if (hm) {
        sq.classList.add('highlight');
        if (hm.capture) sq.classList.add('capture-move');
      }

      if ((r + c) % 2 === 1) sq.addEventListener('click', () => onSquareClick(r, c));
      boardEl.appendChild(sq);
    }
  }
  updateCounts();
}

function updateCounts() {
  let redCount = 0, blackCount = 0;
  for (let r = 0; r < 8; r++) {
    for (let c = 0; c < 8; c++) {
      const v = board[r][c];
      if (v) colorOf(v) === 'r' ? redCount++ : blackCount++;
    }
  }
  document.getElementById('redCount').textContent = redCount;
  document.getElementById('blackCount').textContent = blackCount;
}

function setStatus(text) {
  document.getElementById('status').textContent = text;
}

function onSquareClick(r, c) {
  if (gameOver || turn !== 'r' || thinking) return;
  const v = board[r][c];

  const move = highlightedMoves.find(m => m.to[0] === r && m.to[1] === c);
  if (selected && move) {
    applyHumanMove(selected, move);
    return;
  }

  if (v && colorOf(v) === 'r') {
    if (mustCaptureSquares.length > 0 && !mustCaptureSquares.includes(r + ',' + c)) {
      setStatus('You must capture with a highlighted piece!');
      return;
    }
    if (forcedPiece && (forcedPiece[0] !== r || forcedPiece[1] !== c)) return;

    selected = [r, c];
    const jumps = getJumpsForPiece(r, c);
    highlightedMoves = jumps.length > 0
      ? jumps
      : (mustCaptureSquares.length === 0 ? getSimpleMovesForPiece(r, c) : []);
    render();
  }
}

function applyHumanMove(from, move) {
  const [r, c] = from;
  const [nr, nc] = move.to;
  const v = board[r][c];
  board[r][c] = null;

  let newVal = v;
  let promoted = false;
  if (!isKing(v) && colorOf(v) === 'r' && nr === 0) {
    newVal = 'R';
    promoted = true;
  }
  board[nr][nc] = newVal;

  if (move.capture) board[move.capture[0]][move.capture[1]] = null;

  if (move.capture && !promoted) {
    const further = getJumpsForPiece(nr, nc);
    if (further.length > 0) {
      selected = [nr, nc];
      forcedPiece = [nr, nc];
      highlightedMoves = further;
      render();
      setStatus('Continue your jump!');
      return;
    }
  }

  selected = null;
  forcedPiece = null;
  highlightedMoves = [];
  render();

  if (!hasAnyMove('b')) {
    gameOver = true;
    setStatus('You win! Black has no moves left.');
    return;
  }

  turn = 'b';
  thinking = true;
  setStatus('Computer is thinking...');
  requestAIMove();
}

// Work out the best move using PHP compute engine

function requestAIMove() {
  fetch('compute.php', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ board, difficulty }),
  })
    .then(res => res.json())
    .then(data => {
      thinking = false;
      if (data.gameOver) {
        gameOver = true;
        setStatus('You win! Computer has no moves left.');
        return;
      }
      board = data.board;
      turn = 'r';
      updateMustCapture();
      render();

      if (!hasAnyMove('r')) {
        gameOver = true;
        setStatus('Computer wins! You have no moves left.');
        return;
      }
      setStatus('Your move (Red)');
    })
    .catch(err => {
      thinking = false;
      setStatus('Error contacting server. Is PHP running?');
      console.error(err);
    });
}

document.getElementById('newGameBtn').addEventListener('click', initBoard);
document.getElementById('difficulty').addEventListener('change', e => {
  difficulty = e.target.value;
});

initBoard();
