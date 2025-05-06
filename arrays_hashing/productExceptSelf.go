package arrays_hashing

// Time complexity: O(n)
// Space complexity: O(1)
func ProductExceptSelf1(nums []int) []int {
	l := len(nums)
	res := make([]int, l)
	for i := range l {
		res[i] = 1
	}

	prefix := 1
	for i := 0; i < l; i++ {
		res[i] = prefix
		prefix *= nums[i]
	}

	suffix := 1
	for i := l - 1; i >= 0; i-- {
		res[i] *= suffix
		suffix *= nums[i]
	}

	return res
}

// Time complexity: O(n)
// Space complexity: O(n)
func ProductExceptSelf2(nums []int) []int {
	l := len(nums)
	res := make([]int, l)
	prefix := make([]int, l)
	suffix := make([]int, l)

	prefix[0] = 1
	for i := 1; i < l; i++ {
		prefix[i] = prefix[i-1] * nums[i-1]
	}

	suffix[l-1] = 1
	for i := l - 2; i >= 0; i-- {
		suffix[i] = suffix[i+1] * nums[i+1]
	}

	for i := 0; i < l; i++ {
		res[i] = prefix[i] * suffix[i]
	}

	return res
}
