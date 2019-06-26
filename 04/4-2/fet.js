function randcookie(){
    // 生成随机字符串用作cookie值
    var header = randints(9, 3, 0);
    var middle = randstrs(5);
    var footer = randints(9, 6, 0);
    var pp = randstrs(3);
    var res = header + middle + footer + pp
    return res;
}

function randints(r, n, tof){
    /* 生成随机数字，tof决定返回number类型或者字符串类型
       r 代表数字范围 n 代表数量
    */

    var result = [];
    if(tof){
        return Math.floor(Math.random()*r);
    }
    for(var i=0;i<n;i++){
        s = Math.floor(Math.random()*r);
        result.push(s);
    }
    return result.join('');
}

function randstrs(n){
    // 生成随机字母，n为随机字母的数量
    var result = [];
    for(var i=0; i<n; i++){
        s = String.fromCharCode(65+randints(25, 1, 1));
        result.push(s);
    }
    return result.join('');
}

// 设置Cookie
document.cookie = 'auth=' + randcookie();
// 跳转到指定页面
location.href = '/index.html';