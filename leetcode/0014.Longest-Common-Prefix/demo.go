package leetcode

import "strings"

func demo(strs []string) (res string) {

	if len(strs) == 0 {
		res = ""
		return
	}

	// 取第一个字符串作为基准
	prefix := strs[0]

	for _, k := range strs {

		// 必须从第一个字符串中开始匹配
		for strings.Index(k, prefix) != 0 {
			if len(prefix) == 0 {
				return ""
			}
			prefix = prefix[:len(prefix)-1]
		}
	}
	return prefix

}
