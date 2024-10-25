function solution(array, commands) {
    var answer = [];
    for(let i of commands) {
        let [start, end, k] = i;
        let sorted = array.slice(start - 1, end).sort((a, b) => a - b);
        answer.push(sorted[k - 1])
    }
    return answer;
}