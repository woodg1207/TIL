def palindrome(word): # naan
    list_word = list(word) #[n a a n]
    #리스트 요소의 양쪽 끝끼리 계속 비교하면서 진행
    for i in range(len(list_word) // 2): #2가나온다.
        if list_word[i] !=list_word[-i-1]:
            return False
    return True

a = input('')
print(palindrome(a))


