<?php
header('Content-Type: application/json');

$input = json_decode(file_get_contents('php://input'), true);
$board = $input['board'] ?? null;
$difficulty = $input['difficulty'] ?? 'medium';
$aiColor = 'b'; // computer always plays black

if (!$board) {
    echo json_encode(['error' => 'No board supplied']);
    exit;
}

$depthMap = ['easy' => 1, 'medium' => 4, 'hard' => 6];
$depth = $depthMap[$difficulty] ?? 4;

function inBounds($r, $c) { return $r >= 0 && $r < 8 && $c >= 0 && $c < 8; }
function isKingPiece($v) { return $v === 'R' || $v === 'B'; }
function colorOf($v) { if ($v === null) return null; return strtolower($v) === 'r' ? 'r' : 'b'; }
function oppColor($c) { return $c === 'r' ? 'b' : 'r'; }

function forwardDirs($color, $king) {
    if ($king) return [[-1, -1], [-1, 1], [1, -1], [1, 1]];
    return $color === 'r' ? [[-1, -1], [-1, 1]] : [[1, -1], [1, 1]];
}

function cloneBoard($b) { return array_map(fn($row) => $row, $b); }

// Recursively finds all maximal capture chains for one piece.
function findJumpSequences($board, $r, $c, $color, $king, $path, $captured) {
    $results = [];
    foreach (forwardDirs($color, $king) as $d) {
        $mr = $r + $d[0]; $mc = $c + $d[1];
        $lr = $r + 2 * $d[0]; $lc = $c + 2 * $d[1];
        if (!inBounds($lr, $lc)) continue;

        $midVal = $board[$mr][$mc];
        if ($midVal === null || colorOf($midVal) !== oppColor($color)) continue;
        if ($board[$lr][$lc] !== null) continue;

        $newBoard = cloneBoard($board);
        $newBoard[$mr][$mc] = null;
        $newBoard[$r][$c] = null;

        $pieceVal = $king ? ($color === 'r' ? 'R' : 'B') : $color;
        $promoted = false;
        if (!$king) {
            if (($color === 'r' && $lr === 0) || ($color === 'b' && $lr === 7)) {
                $pieceVal = $color === 'r' ? 'R' : 'B';
                $promoted = true;
            }
        }
        $newBoard[$lr][$lc] = $pieceVal;

        $newPath = $path;
        $newPath[] = ['from' => [$r, $c], 'to' => [$lr, $lc], 'capture' => [$mr, $mc]];
        $newCaptured = $captured;
        $newCaptured[] = [$mr, $mc];

        if ($promoted) {
            $results[] = ['path' => $newPath, 'board' => $newBoard, 'captured' => $newCaptured];
        } else {
            $further = findJumpSequences($newBoard, $lr, $lc, $color, $king, $newPath, $newCaptured);
            if (count($further) > 0) {
                foreach ($further as $f) $results[] = $f;
            } else {
                $results[] = ['path' => $newPath, 'board' => $newBoard, 'captured' => $newCaptured];
            }
        }
    }
    return $results;
}

function generateFullTurnMoves($board, $color) {
    $captureMoves = [];
    $simpleMoves = [];

    for ($r = 0; $r < 8; $r++) {
        for ($c = 0; $c < 8; $c++) {
            $v = $board[$r][$c];
            if ($v === null || colorOf($v) !== $color) continue;
            $king = isKingPiece($v);

            $seqs = findJumpSequences($board, $r, $c, $color, $king, [], []);
            foreach ($seqs as $s) $captureMoves[] = $s;

            if (count($seqs) === 0) {
                foreach (forwardDirs($color, $king) as $d) {
                    $nr = $r + $d[0]; $nc = $c + $d[1];
                    if (!inBounds($nr, $nc) || $board[$nr][$nc] !== null) continue;

                    $newBoard = cloneBoard($board);
                    $pieceVal = $v;
                    if (!$king) {
                        if (($color === 'r' && $nr === 0) || ($color === 'b' && $nr === 7)) {
                            $pieceVal = $color === 'r' ? 'R' : 'B';
                        }
                    }
                    $newBoard[$r][$c] = null;
                    $newBoard[$nr][$nc] = $pieceVal;

                    $simpleMoves[] = [
                        'path' => [['from' => [$r, $c], 'to' => [$nr, $nc], 'capture' => null]],
                        'board' => $newBoard,
                        'captured' => [],
                    ];
                }
            }
        }
    }

    return count($captureMoves) > 0 ? $captureMoves : $simpleMoves;
}

function evaluate($board, $aiColor) {
    $score = 0;
    for ($r = 0; $r < 8; $r++) {
        for ($c = 0; $c < 8; $c++) {
            $v = $board[$r][$c];
            if ($v === null) continue;
            $col = colorOf($v);
            $king = isKingPiece($v);

            $base = $king ? 1.7 : 1.0;
            $advance = 0;
            if (!$king) {
                $advance = $col === 'r' ? (7 - $r) * 0.03 : $r * 0.03;
            }
            $centerBonus = (3.5 - abs(3.5 - $c)) * 0.02;
            $val = $base + $advance + $centerBonus;

            $score += ($col === $aiColor) ? $val : -$val;
        }
    }
    return $score;
}

function minimax($board, $depth, $alpha, $beta, $maximizing, $aiColor) {
    $currentColor = $maximizing ? $aiColor : oppColor($aiColor);
    $moves = generateFullTurnMoves($board, $currentColor);

    if (count($moves) === 0) {
        return $maximizing ? -1000 : 1000; // current side to move has no moves = loses
    }
    if ($depth === 0) {
        return evaluate($board, $aiColor);
    }

    if ($maximizing) {
        $best = -INF;
        foreach ($moves as $m) {
            $val = minimax($m['board'], $depth - 1, $alpha, $beta, false, $aiColor);
            $best = max($best, $val);
            $alpha = max($alpha, $best);
            if ($beta <= $alpha) break;
        }
        return $best;
    } else {
        $best = INF;
        foreach ($moves as $m) {
            $val = minimax($m['board'], $depth - 1, $alpha, $beta, true, $aiColor);
            $best = min($best, $val);
            $beta = min($beta, $best);
            if ($beta <= $alpha) break;
        }
        return $best;
    }
}

$moves = generateFullTurnMoves($board, $aiColor);

if (count($moves) === 0) {
    echo json_encode(['gameOver' => true, 'winner' => 'r']);
    exit;
}

if ($difficulty === 'easy') {
    // Weak play: pick randomly among a handful of legal moves (captures still enforced).
    shuffle($moves);
    $chosen = $moves[array_rand(array_slice($moves, 0, min(3, count($moves))))];
} else {
    $bestScore = -INF;
    $bestMoves = [];
    foreach ($moves as $m) {
        $val = minimax($m['board'], $depth - 1, -INF, INF, false, $aiColor);
        if ($val > $bestScore + 0.0001) {
            $bestScore = $val;
            $bestMoves = [$m];
        } elseif (abs($val - $bestScore) < 0.0001) {
            $bestMoves[] = $m;
        }
    }
    $chosen = $bestMoves[array_rand($bestMoves)];
}

echo json_encode([
    'gameOver' => false,
    'path' => $chosen['path'],
    'board' => $chosen['board'],
]);