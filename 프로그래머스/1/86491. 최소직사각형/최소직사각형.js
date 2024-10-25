function solution(sizes) {
    var answer = 0;
    max_a = 0;
    max_b = 0;
    
    for(let i = 0; i < sizes.length; i++) {
        sizes[i].sort((a, b) => a - b);
        max_a = Math.max(max_a, sizes[i][0]);
        max_b = Math.max(max_b, sizes[i][1]);
    }
    answer = max_a * max_b
    return answer;
}