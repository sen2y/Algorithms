function solution(my_string) {
    reverse = []
    for (i in my_string) { 
        reverse.push(my_string[my_string.length -i -1])
    }
    return reverse.join("")
}