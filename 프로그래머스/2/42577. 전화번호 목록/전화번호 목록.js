function solution(phone_book) {
    phone_book.sort()
    
    for (let i = 0; i < phone_book.length - 1; i++) {
        var target = phone_book[i];
        for (let j = i+1; j < phone_book.length; j++) {
            if(phone_book[j].startsWith(target)) {
                return false;
            }
            else break;
        }
    }
    
    return true;
}