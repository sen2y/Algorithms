function solution(my_string) {  
    nums = [...my_string].filter(str => parseInt(str)>0 && parseInt(str)<10)
    return nums.reduce((a,b)=> parseInt(a)+parseInt(b))
}