package arrays_hashing

func IsValidSudoku(board [][]byte) bool {
	// check rows
	for i := 0; i < 9; i++ {
		row := make(map[byte]bool)
		for j := 0; j < 9; j++ {
			if board[i][j] != '.' {
				if row[board[i][j]] {
					return false
				}
				row[board[i][j]] = true
			}
		}
	}

	// check columns
	for i := 0; i < 9; i++ {
		col := make(map[byte]bool)
		for j := 0; j < 9; j++ {
			if board[j][i] != '.' {
				if col[board[j][i]] {
					return false
				}
				col[board[j][i]] = true
			}
		}
	}

	// check boxes
	for boxRow := 0; boxRow < 3; boxRow++ {
		for boxCol := 0; boxCol < 3; boxCol++ {
			box := make(map[byte]bool)
			for i := 0; i < 3; i++ {
				for j := 0; j < 3; j++ {
					if board[boxRow*3+i][boxCol*3+j] != '.' {
						if box[board[boxRow*3+i][boxCol*3+j]] {
							return false
						}
						box[board[boxRow*3+i][boxCol*3+j]] = true
					}
				}
			}
		}
	}

	return true
}
