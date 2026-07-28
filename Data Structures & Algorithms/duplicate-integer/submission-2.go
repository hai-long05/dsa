func hasDuplicate(nums []int) bool {
    seen := make(map[int]bool, len(nums))
    for _, v := range nums {
        if _, ok := seen[v]; ok {
            return true
        }
        seen[v] = true
    }

    return false
}
