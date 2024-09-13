function solution(array, height) {
    answer = array.filter((s)=> s>height)
    return answer.length;
}