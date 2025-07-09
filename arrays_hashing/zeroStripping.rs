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
