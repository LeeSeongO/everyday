def solution(s):
	if len(s) == 1:
		return 1

	s_length = []

	for str_i in range(1, (len(s) // 2) + 1):

		temp = s[:str_i]
		temp_str = ''
		compression_count = 1

		for str_j in range(str_i, len(s), str_i):
			if temp == s[str_j:str_j + str_i]:
				compression_count += 1
			else:
				if compression_count == 1:
					compression_count = ''

				temp_str += str(compression_count) + temp
				temp = s[str_j:str_j + str_i]
				compression_count = 1
			print('check')

		if compression_count == 1:
			compression_count = ''
		temp_str += str(compression_count) + temp
		s_length.append(len(temp_str))

	answer = min(s_length)
	return answer


s_list = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

print(solution(s_list[0]))
