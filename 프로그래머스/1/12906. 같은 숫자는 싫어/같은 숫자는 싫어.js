function solution(arr)
{
    var answer = [];

    arr.forEach((a, idx) => {
        if (idx === 0) answer.push(a)
        if (idx > 0) {
            if(a !== arr[idx-1]) answer.push(a)
        }
    })
    
    return answer;
}