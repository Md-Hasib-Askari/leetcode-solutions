package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	topKFrequent "github.com/Md-Hasib-Askari/leetcode-solutions/arrays_hashing"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
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

	astr, _ := reader.ReadString('\n')
	astr = strings.TrimSpace(astr)
	ainp := strings.Fields(astr)
	a := make([]int, len(ainp))
	for i := 0; i < len(ainp); i++ {
		a[i], _ = strconv.Atoi(ainp[i])
	}

	kstr, _ := reader.ReadString('\n')
	kstr = strings.TrimSpace(kstr)
	k, _ := strconv.Atoi(kstr)

	// Solve problem here
	result := solve(a, k)

	// Print output
	fmt.Fprintln(writer, result)
	// }
}

func solve(nums []int, k int) []int {
	// Solve problem here

	fmt.Println("nums: ", nums)
	fmt.Println("k: ", k)
	res := topKFrequent.TopKFrequent_n(nums, k)
	return res
}
