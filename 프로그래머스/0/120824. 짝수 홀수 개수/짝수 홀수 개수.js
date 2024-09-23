function solution(num_list) {
    const one = num_list.filter((x)=>x%2===1)
    const two = num_list.filter((x)=>x%2===0)
    return [two.length, one.length]
}