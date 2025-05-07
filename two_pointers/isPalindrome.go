package twopointers

import "fmt"

func isAlphaNumeric(ch rune) bool {
	if ch >= '0' && ch <= '9' {
		return true
	}
	if ch >= 'a' && ch <= 'z' {
		return true
	}
	if ch >= 'A' && ch <= 'Z' {
		return true
	}
	return false
}

func IsValidPalindrome(s string) bool {
	var str []rune
	for _, ch := range s {
		if isAlphaNumeric(ch) {
			str = append(str, ch)
		}
	}

	for idx, ch := range str {
		if ch >= 'A' && ch <= 'Z' {
			str[idx] = ch | 0x20 // Convert to lowercase
		}
	}

	for i := 0; i < len(str); i++ {
		fmt.Printf("%c ", str[i])
	}

	// Check if the string is a palindrome
	for i, j := 0, len(str)-1; i < j; i, j = i+1, j-1 {
		if str[i] != str[j] {
			return false
		}
	}

	return true
}
