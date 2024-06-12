function solution(players, callings) { 
    dic = {}
    for (let i=0; i<players.length; i++ ){
        dic[players[i]] = i;
    } 
    for (let i=0; i<callings.length; i++){ ;
        let calledPlayer = callings[i];
        let idx = dic[calledPlayer];
        if (idx == 0) continue;  
        dic[players[idx]] = idx-1;
        dic[players[idx-1]] = idx; 
        players[idx] = players[idx-1];
        players[idx-1] = calledPlayer;  
    }
    return players;
}