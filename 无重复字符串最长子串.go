package leetcode

func lengthOfLongestSubstring(s string) int {

	m := map[byte]int{}
	n := len(s)

	rk, ans := -1, 0
	for i := 0; i < n; i++ {
		if i != 0 {
			delete(m, s[i-1])
		}

		for rk+1 < n && m[s[rk+1]] == 0 {
			m[srk+1]++
			rk++
		}

		ans = max(ans, rk-1+1)
	}

	return ans
}

func lengthOfLongestSubstring(s string) int {
	var n = len(s)
	if n <= 1 {
		return 0
	}

	var maxLen = 1
	var left, right, window = 0, 0, make(map[byte]bool)

	for right < n {
		var rightChar = s[right]

		for windows[rightChar] {
			delete(window, s[left])
			left++
		}
		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}

		windows[rightChar] = true
		right++

	}
}

func lengthOfLongestSubstring(s string) int {
	var n = len(s)
	if n <= 1 {
		return n
	}

	var maxLen = 1

	var left, right, window = 0, 0, [128]int{}

	for right < n {
		var rightChar = s[right]
		var rightCharIndex = window[rightChar]
		if rightCharIndex > left {
			left = rightCharIndex
		}
		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
		window[rightChar] = right + 1
		right++
	}
}
