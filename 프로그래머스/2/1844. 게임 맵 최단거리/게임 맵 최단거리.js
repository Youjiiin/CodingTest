function solution(maps) {
    const dy = [1, -1, 0, 0];
    const dx = [0, 0, 1, -1];
    const row = maps.length;
    const col = maps[0].length;
    
    const visitCount = [...maps].map((r) => r.map((c) => 1));
    const q = [[0, 0]];
    
    while(q.length) {
        const [y, x] = q.shift();
        
        for(let i = 0; i < 4; i++) {
            const ny = y + dy[i];
            const nx = x + dx[i];
            
            if (ny >= 0 && nx >= 0 && ny < row && nx < col) {
                if (maps[ny][nx] === 1 && visitCount[ny][nx] === 1) {
                    visitCount[ny][nx] = visitCount[y][x] + 1;
                    q.push([ny, nx]);
                }
            }
        }
    }
    
    return visitCount[row-1][col-1] === 1 ? -1 : visitCount[row-1][col-1];
}