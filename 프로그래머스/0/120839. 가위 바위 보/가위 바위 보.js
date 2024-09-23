function solution(rsp) {
    results = []
    for (v of [...rsp]){
        if (v==0) results.push(5)
        if (v==2) results.push(0)
        if (v==5) results.push(2)
    }
    return results.join("")
}