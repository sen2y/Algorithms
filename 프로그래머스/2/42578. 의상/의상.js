function solution(clothes) {
    let ans = {}
    clothes.forEach(el => { 
        if (ans[el[1]]) return ans[el[1]]++
        ans[el[1]] = 1
    })
    const arr = Object.values(ans)   
    const num = arr.length > 1 ? arr.reduce((a,b)=>(a+1)*(b+1)-1) : clothes.length
    return num
}