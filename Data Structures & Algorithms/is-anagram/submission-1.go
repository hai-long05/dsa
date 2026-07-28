func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sMap := make(map[string]int)
	tMap := make(map[string]int)

	for i, _ := range s {
		sMap[string(s[i])] = sMap[string(s[i])] + 1
		tMap[string(t[i])] = tMap[string(t[i])] + 1
	}

	for k, v := range sMap {
		if tMap[k] != v {
			return false
		} 
	}

	return true
}
