/* 计算型验证码 
验证逻辑：记录数值与运算符
1、获取用户输入的数值
2、将用户输入数值与程序得到的数值比对，相同则通过验证
*/

function multMath(){
    // 乘法
    var first = randNumber(1, 20);
    var second = randNumber(5, 15);
    return [first, second, '*']
}

function additionMath(){
    // 加法
    var first = randNumber(20, 99);
    var second = randNumber(3, 99);
    return [first, second, '+']
}

function subMath(){
    // 减法
    var first = randNumber(46, 99);
    var second = randNumber(1, 45);
    return [first, second, '-']
}

var mathesResult = [];  // Canvas 生成的验证码

$(function(){
    var matchesCanvas = document.getElementById('matchesCanvas');
    var cvas = matchesCanvas.getContext('2d');
    // 获取计算题目
    var mathList = [multMath(), additionMath(), subMath()];
    var i = (randNumber(0, mathList.length));
    var maths = mathList[i]

    var width = matchesCanvas.width - 20; var height = matchesCanvas.height;
    // 先绘制背景色
    cvas.fillStyle = `#CDC8B1`;
    cvas.fillRect(0, 0, width, height)

    // 再绘制计算题目
    cvas.fillStyle = `#7F7F7F`;
    var fontSize = 26;
    cvas.font = fontSize +'px Arial';
    cvas.textBaseline = 'middle';
    cvas.fillText(maths[0], 10, 20);
    cvas.fillText(maths[2], 50, 20);
    cvas.fillText(maths[1], 80, 20);
    cvas.fillText('= ?', 120, 20);
    if(i == 0){
        var result = parseInt(maths[0]) * parseInt(maths[1]);
    }else if(i == 1){
        var result = parseInt(maths[0]) + parseInt(maths[1]);
    }else{
        var result = parseInt(maths[0]) - parseInt(maths[1]);
    }
    // 给出计算结果
    mathesResult.push(result);
})


function mathesVerify(){
    // 计算型验证码用户输入结果
    var codeInt = parseInt(mathesResult.join(''));
    var inputCode = parseInt(document.getElementById('code').value);
    if(inputCode==codeInt){
        alert('计算结果：' + inputCode + '，通过验证。');
    }else{
        alert('很遗憾，未通过验证');
    }
}
