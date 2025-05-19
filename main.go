package main

import (
	"bufio"
	"fmt"
	"os"

	two_pointers "github.com/Md-Hasib-Askari/leetcode-solutions/two_pointers"
)

func main() {
	// reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	// Read number of test cases
	// tStr, _ := reader.ReadString('\n')
	// t, _ := strconv.Atoi(strings.TrimSpace(tStr))

	// for i := 0; i < t; i++ {
	// Read input
	// nstr, _ := reader.ReadString('\n')
	// ninp := strings.Fields(nstr)
	// n, _ := strconv.ParseInt(ninp[0], 10, 64)

	// astr, _ := reader.ReadString('\n')
	// astr = strings.TrimSpace(astr)
	// ainp := strings.Fields(astr)
	// a := make([]int, len(ainp))
	// for i := 0; i < len(ainp); i++ {
	// 	a[i], _ = strconv.Atoi(ainp[i])
	// }

	// Solve problem here
	result := solve()

	// Print output
	fmt.Fprintln(writer, result)
	// }
}

func solve() []int {
	// Solve problem here
	numbers := []int{-1, 0}
	target := -1
	result := two_pointers.TwoSum(numbers, target)

	return result

}
