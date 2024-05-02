function solution(my_string, indices) {
    indices.sort((a,b) => b-a)
    let arr = [];
    for (let i = 0; i < my_string.length ; i++){
        const index = indices[indices.length-1]
        if ( index == i ){
            indices.pop();
            continue;
        }
        
        else arr.push(my_string[i])
    }
    return arr.join("")
    
}