function solution(phone_book) { 
    phone_book.sort() 
    const len = phone_book.length
    for (let i=1; i<len; i++){ 
        if (phone_book[i].startsWith(phone_book[i-1])) return false;
 
    } 
   return true
}