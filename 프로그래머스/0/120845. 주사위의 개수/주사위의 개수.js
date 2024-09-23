function solution(box, n) {
    const [a, b, c] = box
    return (parseInt(a/n) * parseInt(b/n) * parseInt(c/n))
}