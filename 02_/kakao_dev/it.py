def solution(expression):
    answer = 0

    d = {
        0:'*',
        1:'+',
        2:'-',
    }
    for i in range(3):
        for j in range(3):
            if j==i: continue
            for k in range(3):
                if k==j or k==i: continue
                prior = [d[i], d[j], d[k]]
                numbers = []
                cal = []
                n = ''
                for num in expression:
                    if num in '*+-':
                        numbers.append(n) 
                        cal.append(num)
                        n=''
                        continue
                    n+= num
                numbers.append(int(n))
    return numbers




sample = "100-200*300-500+20"	
print(solution(sample))