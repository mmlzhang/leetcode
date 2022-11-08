package main

import (
	"strconv"
	"strings"
)

func myAtoi(s string) int {
	s = strings.Trim(s, " ")

	flag := 1
	if len(s) == 0 {
		return 0
	}

	first := s[0:1]

	if first == "-" {
		flag = -1
		s = s[1:]
	} else if first == "+" {
		flag = 1
		s = s[1:]
	}

	result := 0
	var max_v int = 2147483647
	var min_v int = -2147483648

	// for i := 0; i< len(s); i ++ {
	// 	ch := s[i]
	// }

	for _, ch1 := range s {
		val, err := strconv.Atoi(string(ch1))
		if err == nil {
			result = result*10 + val
			if result >= max_v && flag == 1 {
				return max_v
			} else if result >= -min_v && flag == -1 {
				return min_v
			}
		} else {
			return result * flag
		}
	}

	return result * flag

}

func main() {

}
