package sort

import "fmt"

func main() {
	arr := []int{1, 4, 6, 2, 22, 55, 22, 33, 11, 4, 6, 8}
	fmt.Println(QuickSort(arr))

}

func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	splitdata := arr[0]
	low := make([]int, 0, 0)
	high := make([]int, 0, 0)
	mid := make([]int, 0, 0)
	mid = append(mid, splitdata)

	for i := 1; i < len(arr); i++ {
		if arr[i] < splitdata {
			low = append(low, arr[i])
		} else if arr[i] > splitdata {
			hight = append(hight, arr[i])
		} else {
			mid = append(mid, arr[i])
		}
	}
	low, hight = QuickSort(low), QuickSort(hight)
	myarr := append(append(low, mid...), hight...)
	return myarr
}
