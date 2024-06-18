function solution(todo_list, finished) {
    return todo_list.filter((list, idx) => finished[idx] == false)
}