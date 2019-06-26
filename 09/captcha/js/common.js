var fontSize = 18; // 字体大小
var fonts = fontSize +'px Arial';


function randNumber(min, max){
    // 随机数方法
    var res = parseInt(Math.random() * (max - min) + min);
    return res;
}

function randColor(min, max){
    // 随机色方法
    var r = randNumber(min, max); var g = randNumber(min, max); var b = randNumber(min, max);
    var colorRes = `rgb(${r}, ${b}, ${b})`;
    return colorRes;
}