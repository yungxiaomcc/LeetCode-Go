package leetcode

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for k, v := range nums {
		// m[target-v] 获取另外一半数字的下标
		if idx, ok := m[target-v]; ok {
			return []int{idx, k}
		}
		m[v] = k
	}
	return nil
}
