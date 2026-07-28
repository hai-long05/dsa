func twoSum(nums []int, target int) []int {
    dMap := make(map[int]int, len(nums))

	for i, n := range nums {
		d := target - n
		if _, ok := dMap[d]; ok {
			return []int{dMap[d], i}
		}
		dMap[n] = i
	}

	return []int{-1, -1}
}
