def solution(phone_book):

    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book)-1):
        print(phone_book[i])
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False

    return True

phone_book=["119", "97674223", "1195524421"]	
print(solution(phone_book))