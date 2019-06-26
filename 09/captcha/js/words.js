/* 静态图片验证码 
验证逻辑：记录程序生成的随机字符
1、获取用户输入的内容
2、将用户输入内容关于随机字符比对
相同则通过验证
*/

var strs = [];  // Canvas 生成的验证码
var fontSize = randNumber(28, 40); // 字体大小
var fonts = fontSize +'px Arial';


function cvasInterfere(cvas, width, height){
    // 浅色干扰线
    for(var i=0;i<3;i++){
        cvas.beginPath();
        cvas.moveTo(randNumber(0, width),randNumber(0, height));
        cvas.lineTo(randNumber(0, width),randNumber(0, height));
        cvas.strokeStyle=randColor(180, 260);
        cvas.closePath();
        cvas.stroke();
    }
    // 浅色干扰噪点
    for(var i=0;i<80;i++){
        cvas.beginPath();
        cvas.arc(randNumber(0, width),randNumber(0, height), 1, 0, 2 * Math.PI);
        cvas.closePath();
        cvas.fillStyle=randColor(150, 260);
        cvas.fill();
    }
}


$(function(){
    var wordsCanvas = document.getElementById('wordsCanvas');
    var cvas = wordsCanvas.getContext('2d');
    var letter = "ABCDEFGHJKLIMNPQRSTUVWSYZ1234567890";
    var width = wordsCanvas.width; var height = wordsCanvas.height;
    // 绘制底色
    cvas.fillStyle = randColor(120, 230);
    cvas.fillRect(0, 0, width, height);
    for(var i=0;i<6;i++){
        var single = letter[randNumber(0, letter.length)];  // 从字符集中随机取字
        cvas.font = fonts;
        cvas.textBaseline = 'top';
        cvas.fillStyle=randColor(80, 180);
        cvas.save();
        cvas.translate( 30 * i + 15 , 15);
        cvas.fillText(single, -15 + 5, -15);
        cvas.restore();
        strs.push(single)
    }
     
    // 为验证码加上浅色干扰线和噪点
    cvasInterfere(cvas, width, height)
})

function verifys(){
    // 静态图片验证码用户输入结果
    var codeStr = strs.join('').toLowerCase();
    var inputCode = document.getElementById('code').value.toLowerCase();
    if(inputCode==codeStr){
        alert('验证码：' + inputCode + '，通过验证。');
    }else{
        alert('很遗憾，未通过验证');
    }
}

