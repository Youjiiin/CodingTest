function solution(triangle) {
    let answer = 0;
    let Arr =[];
    let Sum=[];
    for(var i=0; i<triangle.length; i++){
        Sum[i]=[];
        Arr[i]=[];
        for(var j=0; j<triangle[i].length; j++)  Arr[i].push(parseInt(triangle[i][j]))
    }
    Sum[triangle.length-1]=Arr[triangle.length-1];
    Sum[triangle.length-1]=Arr[triangle.length-1];
    for(var i= 1; i<triangle.length; i++){
        for(var j=0; j<Arr[triangle.length-i-1].length;j++){
            Sum[triangle.length-i-1][j]=Math.max(Sum[triangle.length-i][j],Sum[triangle.length-i][j+1])+Arr[triangle.length-i-1][j]
        }
    }
    answer=Sum[0][0];
    return answer;
}