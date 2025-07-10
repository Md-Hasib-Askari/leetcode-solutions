// https://leetcode.com/problems/set-matrix-zeroes/description/

use std::collections::HashSet;

fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
    let mut rows = HashSet::new();
    let mut cols = HashSet::new();

    // First pass: find all the rows and columns that need to be zeroed
    for i in 0..matrix.len() {
        for j in 0..matrix[i].len() {
            if matrix[i][j] == 0 {
                rows.insert(i);
                cols.insert(j);
            }
        }
    }

    // Second pass: set the identified rows and columns to zero
    for i in 0..matrix.len() {
        for j in 0..matrix[i].len() {
            if rows.contains(&i) || cols.contains(&j) {
                matrix[i][j] = 0;
            }
        }
    }
}

fn set_zeroes_improved(matrix: &mut Vec<Vec<i32>>) {
    let mut first_row_zero = false;
    let mut first_col_zero = false;

    // Check if the first row needs to be zeroed
    for j in 0..matrix[0].len() {
        if matrix[0][j] == 0 {
            first_row_zero = true;
            break;
        }
    }

    // Check if the first column needs to be zeroed
    for i in 0..matrix.len() {
        if matrix[i][0] == 0 {
            first_col_zero = true;
            break;
        }
    }

    // Use the first row and column to mark zeroes
    for i in 1..matrix.len() {
        for j in 1..matrix[i].len() {
            if matrix[i][j] == 0 {
                matrix[i][0] = 0; // Mark the first column
                matrix[0][j] = 0; // Mark the first row
            }
        }
    }

    // Zero out cells based on marks in the first row and column
    for i in 1..matrix.len() {
        for j in 1..matrix[i].len() {
            if matrix[i][0] == 0 || matrix[0][j] == 0 {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first row if needed
    if first_row_zero {
        for j in 0..matrix[0].len() {
            matrix[0][j] = 0;
        }
    }

    // Zero out the first column if needed
    if first_col_zero {
        for i in 0..matrix.len() {
            matrix[i][0] = 0;
        }
    }
}

pub fn solve() {
    let mut matrix = vec![
        vec![1, 1, 1, 0],
        vec![1, 0, 1, 1],
        vec![1, 1, 1, 1],
        vec![0, 1, 1, 1],
    ];

    set_zeroes(&mut matrix);

    for row in matrix {
        println!("{:?}", row);
    }
}
