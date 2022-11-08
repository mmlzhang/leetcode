package main

import (
	"fmt"
	"testing"
)

func TestaddTwoNumbers(t *testing.T) {
	l1 := ListNode{Val: 4, Next: &ListNode{Val: 6, Next: &ListNode{Val: 8, Next: nil}}}
	l2 := ListNode{Val: 7, Next: &ListNode{Val: 9, Next: &ListNode{Val: 2, Next: nil}}}

	result := addTwoNumbers(&l1, &l2)

	fmt.Println(result)
}
