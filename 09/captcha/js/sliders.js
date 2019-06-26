/* 滑动验证码 
验证逻辑：滑块释放位置-滑块起始位置-滑轨长度等于滑块宽度，允许误差3
如果值在范围内则通过验证
*/
$(function(){
    
    var tracks = document.getElementById('tracks'),
    sliderblock = document.getElementById('sliderblock'),
    slidertips = document.getElementById('slidertips')  
    // 滑块宽度
    var sliderblockWidth = $('#sliderblock').width();
    // 滑轨长度
    var tracksWidth = $('#tracks').width();
    
    var mousemove = false; // mousedown状态
    sliderblock.addEventListener('mousedown', function (e) {
        // 监听mousedown事件，记录滑块起始位置
        mousemove = true;  // 鼠标按下时，mousedown 状态改变
        startCoordinateX = e.clientX  // 滑块起始位置
      });

      
      var distanceCoordianteX = 0; // 滑块起始位置
      tracks.addEventListener('mousemove', function (e) {
          //监听鼠标移动
          if (mousemove) {// 鼠标点击滑块后才跟踪移动
              distanceCoordianteX = e.clientX - startCoordinateX;  // 滑块当前位置
              if (distanceCoordianteX > tracksWidth - sliderblockWidth) {
                  // 通过限制滑块位移距离，避免滑块向右移出滑轨
                  distanceCoordianteX = tracksWidth - sliderblockWidth;
              } else if (distanceCoordianteX < 0) {
                  // 通过限制滑块位移距离，避免滑块向左移出滑轨
                  distanceCoordianteX = 0;
              }
              // 根据移动距离显示滑块位置
              sliderblock.style.left = distanceCoordianteX + 'px';
          }
      })
          
      sliderblock.addEventListener('mouseup', function (e){
          // 鼠标松开视为完成滑动，记录滑块当前位置并调用验证方法
          var endCoordinateX = e.clientX;
          verifySliderRetuls(endCoordinateX);
      })

      function verifySliderRetuls(endCoordinateX){// 验证滑动结果
        mousemove = false;  // 此时鼠标已松开，防止滑块跟随鼠标移动
        // 允许误差3像素。
        if (Math.abs(endCoordinateX - startCoordinateX - tracksWidth) < sliderblockWidth + 3) {
            // 验证通过后设置提示样式
            sliderblock.style.color = '#666';
            sliderblock.style.fontSize = '28px';
            sliderblock.style.backgroundColor = '#fff';
            sliderblock.innerHTML = '✓';
            slidertips.style['visibility'] = 'visible';
            console.log('验证成功');
        } else {
            // 如果验证失败，滑块复位
            distanceCoordianteX = 0;
            sliderblock.style.left = 0;
            console.log('验证失败');
        }
    }
})
