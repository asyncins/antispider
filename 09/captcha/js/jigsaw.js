/* 拼图验证码
验证逻辑：
1、记录缺口位置
2、在鼠标按下和松开时记录鼠标的相对位置
3、鼠标松开时的位置与按下时的位置差值与缺口位置比较，在范围内则认为通过
*/


var jigsaw = $('.jigsaw'), jigsawTrack = $('.jigsawTrack'),
    jigsawCircle = $('.jigsawCircle'), jigsawTips = $('.jigsawTips'), 
    missblock = $('.missblock'), targetblock = $('.targetblock')

$(function() {
    var imageback = $('.imageback') // 背景图所在标签
    imageback.attr('src', `images/1.jpg`) // 背景图
    missblock.css('background-image', `url('images/0.jpg')`)  // 对应的滑块
  var imageback = document.getElementById('imageback');
    imageback.onload = function() {
      // 获取图片高度
      var imageHeight = this.clientHeight
      // 生成缺口坐标
      var CoordinateX = 150/2 * (1 + Math.random()), CoordinateY = Math.random() * imageHeight / 2
      // 鼠标按下
      fnDown(CoordinateX , CoordinateY)
    
  }
})

function fnDown(CoordinateX, CoordinateY) {
    jigsawCircle.mousedown(function(e) {
    e.stopPropagation()  
    // 鼠标按下时，显示圆角矩形的位置
   var missblockFirst = 10;
    missblock.css('left', `${missblockFirst}px`)
    // 鼠标按下时，滑块的位置
    var circleMousedown = jigsawCircle.offset().left
    var missblockWidth = missblock.width();
    var missblockWidthHalf = missblockWidth/2;
    // 缺块显示
    missblock.css({
      display: 'block',
      top: `${CoordinateY}px`,
      'background-position': `-${CoordinateX - missblockWidth/3}px -${CoordinateY - missblockWidth/2}px`
    })
    // 缺口位置显示
    targetblock.css({ display: 'block', left: `${CoordinateX}px`, top: `${CoordinateY}px` })
     var distanceX = e.clientX - $(this).offset().left;
      // 提示文字设为透明
      jigsawTips.css('opacity', '0')

    // 监听鼠标移动事件
    jigsaw.bind('mousemove', function(e) {
      fnMove(e, distanceX)
    })

    // 监听mouseup，根据滑块位置判断结果
    jigsaw.bind('mouseup', function() {
    var circleMouseup = jigsawCircle.offset().left;
    var verifyPosition = circleMouseup - circleMousedown
    console.log('缺口位置：' + CoordinateX)
    console.log('circle Mouseup:' + circleMouseup + '-减去-' + 'circle Mousedown:' + circleMousedown)
      // 误差在2px以内则算成功
    if (Math.abs(verifyPosition - CoordinateX + 10) > 2) {
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

function fnMove(e, distanceX) {
// 滑块移动范围控制在滑轨中，不可超出
  var l = e.clientX - distanceX - $(jigsawTrack).offset().left, winW = $(jigsawTrack).width() + 29
  if (l < 0) {l = 0} else if (l > winW) {l = winW}
  jigsawCircle.css('left', `${l}px`)
  missblock.css('left', `${l + 10}px`)
}