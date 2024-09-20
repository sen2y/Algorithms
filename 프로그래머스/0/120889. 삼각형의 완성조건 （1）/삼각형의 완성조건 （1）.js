function solution(sides) {
    // 내림차순
    sortArr = sides.sort(function (a,b) {return b-a}) 
    return sortArr[0] < sortArr[1] + sortArr[2] ? 1 : 2
    
}