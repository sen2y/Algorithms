function solution(my_string) {
    let a = [...my_string].filter(x=>!['a','e','i','o','u'].includes(x))
    return a.join("")
}