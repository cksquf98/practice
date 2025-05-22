function solution(numbers) {
    var answer = '';
    answer = numbers.sort((a, b)=>{
        a = a.toString();
        b = b.toString();
        
        return (b+a) - (a+b);
    }).join('')
    
    
    return answer[0] === '0' ? '0' : answer;
}