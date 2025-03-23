package arrays_hashing

import "sort"

// Time complexity: O(nlogn)
// Space complexity: O(n)
func TopKFrequent_nlogn(nums []int, k int) []int {
	freq := make(map[int]int)
	for _, v := range nums {
		if _, ok := freq[v]; !ok {
			freq[v] = 1
		} else {
			freq[v]++
		}
	}

	sorted := make([]int, 0, len(freq))
	for ky := range freq {
		sorted = append(sorted, ky)
	}
	sort.Slice(sorted, func(i, j int) bool {
		return freq[sorted[i]] > freq[sorted[j]]
	})

	res := make([]int, 0, k)
	for i := 0; i < int(k); i++ {
		res = append(res, sorted[i])
	}

	return res
}

// Time complexity: O(n)
// Space complexity: O(n)
func TopKFrequent_n(nums []int, k int) []int {
	freq := make(map[int]int)
	for _, v := range nums {
		if _, ok := freq[v]; !ok {
			freq[v] = 1
		} else {
			freq[v]++
		}
	}

	bucket := make([][]int, len(nums)+1)
	for ky, v := range freq {
		if bucket[v] == nil {
			bucket[v] = make([]int, 0)
		}
		bucket[v] = append(bucket[v], ky)
	}

	res := make([]int, 0, k)
	for i := len(bucket) - 1; i >= 0; i-- {
		if bucket[i] != nil {
			for _, v := range bucket[i] {
				res = append(res, v)
				if len(res) == k {
					return res
				}
			}
		}
	}

	return res
}
