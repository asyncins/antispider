/* 点选验证码 */

getChinese=function(){
    // 随机汉字
    eval( "var singleStr=" +  '"\\u' + (Math.round(Math.random() * 20901) + 19968).toString(16)+'"');
    return singleStr;
}

$(function(){
    var clickCanvas = document.getElementById('clickCanvas');
    var cvas = clickCanvas.getContext('2d')
    var divTips = document.getElementById('divTips');
    var images = new Image(); 
    var fontSizes = 26; // 字体大小
    images.src = 'images/3.jpg';
    
    images.onload = function doCanvas(){
        cvas.drawImage(images, 0, 0, clickCanvas.width, clickCanvas.height);
        cvas.save();  
        cvas.font = `${fontSizes}px Arial`;
        cvas.fillStyle = '#ffffff';
        var positions = []
        var chineseStr = [];
        var shifted = [];
        var targets = [];
        var randTimes = 0;
        var userClick = [];
        var clickTimes = 0;

        function getPosition(){
            // X 需要按文字顺序安排
            var positionX_1 = randNumber(20, 50);  
            var positionX_2 = randNumber(70, 170); 
            var positionX_3 = randNumber(190, 250); 
            var positionX_4 = randNumber(270, 370); 
            positions = [positionX_1, positionX_2, positionX_3, positionX_4]
        } getPosition();

        function chineseArray(){
            for(var i=0;i<4;i++){
                // 获取汉字并生成一定规律的随机座标
                var positionCommonY = randNumber(50, 220);  // Y 随机
                var positionX = positions[i]; 
                var chinese = getChinese();
                var chineseStrPosition = {chinese, positionX, positionCommonY}
                chineseStr.push(chineseStrPosition)
            }
            console.log(chineseStr)
        }chineseArray();
        
        function canvasChinese(){
            // 绘制文字
            for(var i=0;i<4;i++){
                data = chineseStr[i]
                cvas.fillText(data.chinese, data.positionX, data.positionCommonY)
            }
        }canvasChinese();

        function chinessCopyShow(){
            // 汉字坐标数组拷贝
            var chineseStrCopy = []
            for(var i=0;i<chineseStr.length;i++){
                chineseStrCopy.push(chineseStr[i])
            }

            while (randTimes < 2){
                var randnum = randNumber(0, 4);
                if(shifted.indexOf(randnum)){
                    shifted.push(randnum);
                    var target = chineseStrCopy[randnum]  // 从汉字-坐标数组中随机取子数组
                    targets.push({target, randnum});
                    randTimes += 1;
                }else{
                    console.log('shifted:'+shifted+'-randum:'+randnum)
                }
            }  
            tipsStr0 = targets[0].target.chinese;
            tipsStr1 = targets[1].target.chinese;
            divTips.innerHTML = `请依次点击图中的：“${tipsStr0}” 和 “${tipsStr1}”`
        }chinessCopyShow();

        $('#clickCanvas').bind('mousedown', function(e){
            // 监听点击事件
            e = e || window.event;
            mouseClick(e);
        })
    

        function mouseClick(e){
            //获取canvas相对于浏览器的坐标
            var rect = clickCanvas.getBoundingClientRect();
            //获取鼠标在canvas上的位置
            var x = (e.clientX - rect.left);
            var y = (e.clientY - rect.top);
            coordinates = {x, y};  // 记录点击座标
            userClick.push(coordinates);
            clickTimes += 1;  // 记录点击次数
            if(clickTimes == 2){
                // 点击2次，自动进入判断流程
                data0 = targets[0].target;
                data1 = targets[1].target
                console.log(userClick)
                console.log('targets0:'+data0.chinese+'x:'+data0.positionX+'y:'+data0.positionCommonY)
                console.log('targets1:'+data1.chinese+'x:'+data1.positionX+'y:'+data1.positionCommonY)
                clickTimes = 0;
                if(data0.positionX + fontSizes > userClick[0].x && 
                    data0.positionCommonY + fontSizes > userClick[0].y &&
                    data1.positionX + fontSizes > userClick[1].x && 
                    data1.positionCommonY + fontSizes > userClick[1].y){
                    divTips.innerHTML = '通过验证';
                    console.log('ok')
                    }else{

                        divTips.innerHTML = '验证失败';
                        console.log('no!')
                    }
                
            }
    
        }
    }


   

})