function solution(X, Y) {
    let arrx = new Array(10).fill(0);
    let arry = new Array(10).fill(0);
    
    for (x of X) arrx[x]++;
    for (y of Y) arry[y]++;
    
    let result = "";
    
    for (let i=9; i>=0; i--){
        const cnt = Math.min(arrx[i], arry[i])
        result += i.toString().repeat(cnt)
    }
    if (result == "") return "-1";
    if (result[0] == '0') return "0"
    return result
}