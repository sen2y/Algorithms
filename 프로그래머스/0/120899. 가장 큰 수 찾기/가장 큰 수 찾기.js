function solution(array) {
    maxIndex = 0
    for (i in array) {
        if (array[maxIndex] < array[i]) maxIndex = i
    }
    return [array[maxIndex], Number(maxIndex)]
}