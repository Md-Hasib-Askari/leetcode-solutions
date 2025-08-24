package twopointers

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
}
