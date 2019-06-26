function fetch(){
    text=$.ajax({
        type:"GET", async: false,
        url:"http://www.porters.vip/verify/sign/fet" + uri()
    });
    $("#content").html(text.responseText);
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
function uri(){
    var action = randints(9, 5, 0);
    var tim = Math.round(new Date().getTime()/1000).toString();
    var randstr = randstrs(5);
    var hexs = hex_md5(action+tim+randstr);
    args = '?actions=' + action + '&tim=' + tim + '&randstr=' + randstr + '&sign=' + hexs;
    return args;
}