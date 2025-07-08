use std::collections::HashSet;

fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
    let mut rows = vec![HashSet::new(); 9];
    let mut cols = vec![HashSet::new(); 9];
    let mut boxes = vec![HashSet::new(); 9];

    for i in 0..9 {
        for j in 0..9 {
            if board[i][j] == '.' {
                continue;
            }
            let num = board[i][j];
            let box_index = (i / 3) * 3 + j / 3;

            if !rows[i].insert(num) || !cols[j].insert(num) || !boxes[box_index].insert(num) {
                return false;
            }
        }
    }
    true
}

pub fn solve() {
    let board = vec![
        vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        vec!['4', '.', '9', '8', '.', '3', '.', '.', '1'],
        vec!['7', '.', '.', '2', '.', '5', '.', '.', '.'],
        vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ];

    let result = is_valid_sudoku(board);
    println!("Is the Sudoku valid? {}", result);
}
