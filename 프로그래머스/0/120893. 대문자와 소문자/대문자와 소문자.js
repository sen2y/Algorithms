function solution(my_string) {
    let answer = [...my_string].map((str) =>{
        return str === str.toUpperCase() ?
             str.toLowerCase() : str.toUpperCase()
    })
    return answer.join("")
}

