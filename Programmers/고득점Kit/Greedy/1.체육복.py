def solution(n, lost, reserve):
    answer = n

    # lost의 값 중에서 reserve에도 있는 값을 제거한 값들만 담는 리스트
    next_lost = []

    lost = sorted(lost)
    reserve = sorted(reserve)

    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            next_lost.append(l)

    # 잃어버린 학생 기준으로
    # 자신의 왼쪽 학생을 먼저 찾아보고 그 후 오른쪽 학생을 찾아본다.
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

