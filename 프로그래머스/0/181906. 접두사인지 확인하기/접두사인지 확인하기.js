// Boolean 값(True, False)를 숫자로(1,0) 바꾸기 + 
// + 단항 연산자를 사용하여 결과를 숫자로 변환합니다. 따라서 number가 n 또는 m으로 나누어 떨어지지 않으면 0이 되고, 나머지 경우에는 1이 됩니다.


function solution(my_string, is_prefix) {
    
    return +my_string.startsWith(is_prefix) 
}
