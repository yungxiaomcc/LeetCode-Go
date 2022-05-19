package leetcode

import (
	"testing"
)

func Test_demo(t *testing.T) {

	test_case := []string{
		"flow",
		"flight",
		"flower",
	}

	res := demo(test_case)

	t.Errorf("output:%s", res)

}
