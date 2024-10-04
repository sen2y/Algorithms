function solution(n) {
    let arr = []
    for (let i=1; i*i<=n; i++){
        if (n%i === 0) {
            let j = n/i
            arr.push(i)
            if (i!=j) arr.push(j)
        }
    }
    return arr.sort((a,b)=>a-b)
}