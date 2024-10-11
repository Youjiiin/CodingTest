function solution(participant, completion) {
    participant.sort();
    completion.sort();
    
    let answer = '';
    for (let i = 0; i < completion.length; i++) {
        if (participant[i] !== completion[i]) {
            answer = participant[i];
            break;
        }
    }
    
    if (!answer) {
        answer = participant[participant.length-1];
    }
    return answer;
}