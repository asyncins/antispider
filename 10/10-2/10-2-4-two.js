var UglifyJS = require("uglify-js");
// 定义用于混淆的 JavaScript 代码
var code = `
var ins = 1 + 2, ss = "abc";
function pack(a, b){
    return a + b + ss;
};
var pp = pack(ins, 6);
console.log(pp);
`
var astree = UglifyJS.parse(code); // 解析代码并生成语法树

var trans = new UglifyJS.TreeTransformer(function (node) {
    if (node instanceof UglifyJS.AST_String || node instanceof UglifyJS.AST_Number) {// 过滤出 String 对象和 Number 对象   
            // 混淆逻辑
            // 过滤出 String 对象和 Number 对象    
            var charhex = charTo16(node.value);
            node.value = charhex;
            return node; // 更新语法树
        }
    });

// 数字、字母转16进制
function charTo16(s) {
    var result = '';
    for (var i=0; i<s.toString().length; i++) {
            // 用“&#x”作为“\x”的替代，后期换回
            var res = "&#x" + s.toString().charCodeAt(i).toString(16);
            result += res;
        
    }
    return result;
};



astree.transform(trans);  //遍历AST树
var ncode = astree.print_to_string(); //从AST还原成字符串
console.log(ncode.replace(/&#x/g, "\\x"));