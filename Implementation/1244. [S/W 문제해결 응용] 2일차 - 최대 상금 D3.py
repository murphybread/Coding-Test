T = int(input())
for test_case in range(1, T + 1):
    num_str, k = input().split()
    k = int(k)
    sorted_num_str = "".join(sorted(num_str, reverse=True))
    i = 0
    while k > 0:
        if num_str[i] != sorted_num_str[i]:
            for j in range(len(num_str) - 1, i, -1):
                if num_str[j] == sorted_num_str[i]:
                    num_list = list(num_str)
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    num_str = "".join(num_list)
                    k -= 1
                    break
        i += 1
    print(f"#{test_case} {num_str}")
