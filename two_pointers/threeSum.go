package twopointers

func ThreeSum(nums []int) [][]int {
	n := len(nums)
	if n < 3 {
		return [][]int{}
	}

	result := [][]int{}
	// Sort the array
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if nums[i] > nums[j] {
				nums[i], nums[j] = nums[j], nums[i]
			}
		}
	}

	for i := 0; i < n-1; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue // Skip duplicates for the first number
		}
		j := i + 1
		k := n - 1
		for j < k {
			if j > i+1 && nums[j] == nums[j-1] {
				j++ // Skip duplicates for the second number
				continue
			}
			if k < n-1 && nums[k] == nums[k+1] {
				k-- // Skip duplicates for the third number
				continue
			}
			sum := nums[i] + nums[j] + nums[k]
			if sum == 0 {
				result = append(result, []int{nums[i], nums[j], nums[k]})
				for j < k && nums[j] == nums[j+1] {
					j++
				}
				for j < k && nums[k] == nums[k-1] {
					k--
				}
				j++
				k--
			} else if sum < 0 {
				j++
			} else {
				k--
			}
		}
	}

	return result
}
