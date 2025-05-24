function solution(nums) {
    var answer = 0;
    
    const maxLen = nums.length / 2;
    
    const numsSet = new Set(nums);
    
    
    if (numsSet.size < maxLen) {
        answer = numsSet.size;
    }
    else {
        answer = maxLen;
    }
    
    return answer;
}