def solution(numbers, hand):
    answer = []   
    pad = {1:(1,1), 2:(1,2), 3:(1,3), 4:(2,1), 5:(2,2), 6:(2,3), 7:(3,1), 8:(3,2), 9:(3,3), "*":(4,1), 0:(4,2), "#":(4,3)}

    l_start_x, l_start_y = 4,1
    r_start_x, r_start_y = 4,3

    for i in numbers:
        if i in [1,4,7,'*']:
            answer.append('L')
            l_start_x, l_start_y = pad[i]

        elif i in [3,6,9,'#']:
            answer.append('R')
            r_start_x, r_start_y = pad[i]
        else:
            a,b = pad[i]
            if abs(a-l_start_x) + abs(b-l_start_y) > abs(a-r_start_x) + abs(b-r_start_y):
                answer.append('R')
                r_start_x, r_start_y = a,b
            elif abs(a-l_start_x) + abs(b-l_start_y) < abs(a-r_start_x) + abs(b-r_start_y):
                answer.append('L')
                l_start_x, l_start_y = a,b
            else:
                if hand == 'left':
                    answer.append('L')
                    l_start_x, l_start_y = a,b
                else:
                    answer.append('R')
                    r_start_x, r_start_y = a,b
    answer = "".join(answer)
    return answer