<template>
<div style="width: 600px;height:400px"></div>
</template>
<script>
    //1. ECharts最基本的代码结构
    //2. 准备数据[{name:???, value:??? },{}]
    //3. 将type的值设置为pie
    var mCharts = echarts.init(document.querySelector("div"))
    // pieData就是需要设置给饼图的数据, 数组,数组中包含一个又一个的对象, 每一个对象中, 需要有name和value
    var pieData = [
      {
        name: '动作',
        value: 11231
      },
      {
        name: '爱情',
        value: 12673
      },
      {
        name: '悬疑',
        value: 6123
      },
      {
        name: '战争',
        value: 8989
      },
      {
        name: '科幻',
        value: 6700
      },
      {
        name: '喜剧',
        value: 11520
      },
      {
        name: '奇幻',
        value: 9369
      }
    ]
    var option = {
      series: [
        {
          type: 'pie',
          data: pieData,
          label: { // 饼图文字的显示
            show: true, // 显示文字
            //formatter: 'hehe' // 决定文字显示的内容
            formatter: function(arg){
              // console.log(arg)
              return arg.name + '片' + arg.value + '元\n' + arg.percent + '%'
            }
          },
          radius: [25, 150],
          roseType: 'radius', // 南丁格尔图 饼图的每一个区域的半径是不同的
          // selectedMode: 'single' // 选中的效果,能够将选中的区域偏离圆点一小段距离
          selectedMode: 'multiple',
          selectedOffset: 30,
        }
      ]
    }
    mCharts.setOption(option)
  </script>