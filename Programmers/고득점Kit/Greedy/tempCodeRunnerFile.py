def solution(n, lost, reserve):
    answer = n

    next_lost = []

    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            next_lost.append(l)

    for l in next_lost:
        flag = False
        if l-1 in reserve:
            reserve.remove(l-1)
            flag = True
        elif l+1 in reserve:
            reserve.remove(l+1)
            flag = True

        if not flag:
            answer -= 1

    return answer


print(solution(5, [2, 3, 4], [1, 2, 3]))
