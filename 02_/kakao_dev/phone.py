# def dfs(D, l_h, r_h):



def solution(numbers, hand):
    answer = ''
    h_arr = {
        1:[0, 0],
        2:[0, 1],
        3:[0,2],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2],
        0:[3,1],
    }
    l_index = [3, 0]
    r_index = [3, 2]
    for number in numbers:
        if number==4 or number==1 or number==7:
            answer += 'L'
            l_index=h_arr[number]
        elif number==3 or number==6 or number==9:
            answer += 'R'
            r_index = h_arr[number]
        else:
            destination = h_arr[number]
            r_l = abs(destination[0]-l_index[0]) + abs(destination[1]-l_index[1])
            r_r = abs(destination[0]-r_index[0]) + abs(destination[1]-r_index[1])
            if r_l<r_r:
                answer+='L'
                l_index=destination
            elif r_l>r_r:
                answer+='R'
                r_index = destination
            else:
                if hand=='right':
                    answer+='R'
                    r_index = destination
                else:
                    answer+='L'
                    l_index=destination
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]*100
hand = "right"
print(solution(numbers, hand))