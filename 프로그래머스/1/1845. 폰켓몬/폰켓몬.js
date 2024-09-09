function solution(nums) {
    let answer = 0;
    // N/2마리를 계산
    let num = nums.length / 2;
    
    // 중복 제거
    let new_nums = new Set(nums);
    nums = [...new_nums];
    
    // 만약, 종류 수 < 가져갈 수 있는 폰켓몬수 -> 종류 수
    if (nums.length < num) {
        answer = nums.length;
    } else {
        // 종류 수 > 가져갈 수 있는 폰켓몬수 -> 가져갈 수 있는 폰켓몬 수
        answer = num;
    }
    
    return answer;
}