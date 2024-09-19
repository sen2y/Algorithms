const solution = (array) => {
    let dict = {}
    for (v of array) {
        if (!dict[v]) dict[v]=1
        else dict[v]++
    }
    let max = 0 // 최대인 원소값
    let cnt = -1 // 최대수
    array.forEach(v => {
        if (!dict[max]) max = v 
        cnt = Math.max(dict[max],dict[v])
        if (dict[v]==cnt){
            max = v
        }
    }) 
    let lenArr = []
    for (i of array) {
        if (dict[i] === cnt) lenArr.push(i)
    } 
    let setArr = new Set(lenArr)
    if (setArr.size > 1) return -1
    return max
    
}