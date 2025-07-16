package twopointers

<<<<<<< HEAD
func TwoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	for left < right {
		sum := numbers[left] + numbers[right]
		if sum == target {
			return []int{left + 1, right + 1}
		} else if sum < target {
			left++
		} else {
			right--
		}
	}
	return []int{-1, -1} // Return -1 if no solution is found
=======
func TwoSum(nums []int, target int) []int {
	i := 0
	j := len(nums) - 1
	for i < j {
		if nums[i]+nums[j] == target {
			return []int{i + 1, j + 1}
		} else if nums[i]+nums[j] < target {
			i++
		} else {
			j--
		}
	}
	return []int{}
>>>>>>> c38258f (Add threeSum and twoSum implementations with input handling and launch configuration)
}
