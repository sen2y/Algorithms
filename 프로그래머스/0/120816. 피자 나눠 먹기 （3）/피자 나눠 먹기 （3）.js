function solution(slice, n) {
    cnt = 1;
    while (true) {
        if (parseInt(cnt*slice / n) >=1) { 
            return cnt;
        }
        cnt++;
    }
}