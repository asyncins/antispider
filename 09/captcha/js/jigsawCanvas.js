 /* Canvas 拼图 */

var jigsaw = $('.jigsaw'), jigsawTrack = $('.jigsawTrack'),
    jigsawCircle = $('.jigsawCircle'), jigsawTips = $('.jigsawTips'), 
    missblock = $('.missblock'), targetblock = $('.targetblock')

var missblockFirst = 10;

$(function() {
    var jigsawCanvas = document.getElementById('jigsawCanvas');
    var cvas = jigsawCanvas.getContext('2d');
    var jigsawImages = new Image();
    jigsawImages.src = 'images/2.jpg'

    jigsawImages.onload = function start() {
        // 图片加载后将图片绘制到Canvas画布
        var imageHeight = jigsawCanvas.height;
        var imageWidth = jigsawCanvas.width;
        cvas.drawImage(jigsawImages, 0, 0, imageWidth, imageHeight);
        cvas.save();  
        // 根据背景图标签的宽高生成缺口坐标
        var CoordinateX = imageWidth/5 +  imageWidth/2 * Math.random(), CoordinateY = imageHeight / 2 * Math.random()
        mouseDowns(CoordinateX , CoordinateY)
      }
 
    function mouseDowns(CoordinateX, CoordinateY) {
        var targetblockTimes = 0;
        jigsawCircle.mousedown(function(e) {
        e.stopPropagation()
        // 鼠标按下时，滑块的位置
        var circleMousedown = jigsawCircle.offset().left;
        // 圆角矩形显示
        missblock.css({
        display: 'block',
        top: `${CoordinateY}px`,
        'background-position': `-${missblockFirst}px -${CoordinateY}px`
        })
        // 绘制缺口，计数避免重复绘制
        if(targetblockTimes<1){
            var targetImage = new Image();
            targetImage.src = 'images/1.jpg';
            cvas.fillStyle = "rgba(0,0,0,0.6)";
            // 在指定位置绘制38x38大小的矩形
            cvas.fillRect(CoordinateX, CoordinateY, 38, 38); 
            targetblockTimes += 1;
        }else{
            console.log('missblock alredy in canvas')
        }
        // 获取鼠标到按钮的距离
        var disX = e.clientX - $(this).offset().left;
        // 提示文字设为透明
        jigsawTips.css('opacity', '0')
        // 监听鼠标移动事件
        jigsaw.bind('mousemove', function(e) {
        mouseMoves(e, disX)
        })

    // 监听mouseup，根据滑块位置判断结果
    jigsaw.bind('mouseup', function() {
        // 滑块移动距离等于鼠标松开时的X坐标减去鼠标按下时的X坐标
        var circleMouseup = jigsawCircle.offset().left;
        var endPosition = circleMouseup - circleMousedown;
        // 误差在2px以内则算成功
        if (Math.abs(endPosition - CoordinateX + missblockFirst) > 2) {
            console.log('验证失败')
            // 缺块和滑块归位
            jigsawCircle.css('left', '0px');
            missblock.css('left', '10px');
            // 显示提示文字
            jigsawTips.css('opacity', '1');
            } else {
                alert('您已完成拼图，通过验证');
            }
        // 移除鼠标事件监听
        jigsaw.unbind('mousemove')
        jigsaw.unbind('mouseup')
        })
    })
    }
})

function mouseMoves(e, distanceX) {
    // 滑块移动范围控制在滑轨中，不可超出
    var jigsawCirclePosition = e.clientX - distanceX - $(jigsawTrack).offset().left;
    var jigsawTrackWidth = jigsawTrack.width(); // 滑轨长度
    if (jigsawCirclePosition < 0) {
        jigsawCirclePosition = 0
    }else if (jigsawCirclePosition > jigsawTrackWidth) {
        jigsawCirclePosition = jigsawTrackWidth
    }
    //实时显示滑块和圆角矩形的位置
    jigsawCircle.css('left', `${jigsawCirclePosition}px`)
    missblock.css('left', `${jigsawCirclePosition + missblockFirst}px`)
}