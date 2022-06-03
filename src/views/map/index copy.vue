<template>
    <div style="height: 100%; width: 100%" ref="map">
    </div>
</template>

<script> 
import chinaJson from '@/assets/china.json'
import axios from 'axios'
import 'echarts' 

export default {
  name: "Map",
  data() {
    return{
      msg: [],
      datas:[]
    }
  },
  // 先获取后端数据
  
  methods: {
      refresh(){
          this.getdata();
          this.drawMap()   
      },
      getdata() {
        // 使用 axios 向 flask 发送请求
        const url = "http://127.0.0.1:5000/api/getMsg";
        
        this.$nextTick(function(){
          axios.get(url)
          .then((res) => {
            //console.log(res.data)
            this.msg = res.data;
            for (var i = 0; i < res.data.length; i++){
              this.datas.push({
                name:this.msg[i].name,
                value:this.msg[i].value
            })
          }
        }).catch((error) => {
            console.log(error);
          })
      },
      )
      },

      MapInit(chart){
        let option
      chart.setOption(
          (option = {

          // 引入时间轴
          timeline:{
            x:50,
            realtime:false,
            width: 670,
            axisType:'category',
            label:{
              color:'#ffffff',
            },
            playInterval:2000,
          bottom:'6%',
          autoPlay: true,
          loop: true,

          data: ['2020-01', '2020-02','2020-03','2020-04','2020-05','2020-06','2020-07','2020-08',
          '2020-09','2020-10','2020-11','2020-12','2021-01','2021-02','2021-03','2021-04','2021-05',
          '2021-06','2021-07','2021-08','2021-09','2021-10','2021-11','2021-12','2022-01','2022-02',
          '2022-03','2022-04'],
          tooltip:{
            // 显示触发类型, item 在 hover 时显示
              trigger: 'item',
              // 地图 : {b}（区域名称），{c}（合并数值）, {d}（无）
              formatter: '年月：{b}<br/> '
          }
        },
            // 图表标题和副标题
            title: {
              text: 'Corona Virus Disease 2019 in China (2022)',
              subtext: 'Data from website',
              sublink: 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
            },
            // 提示框组件
            tooltip: {
              // 显示触发类型, item 在 hover 时显示
              trigger: 'item',
              // 地图 : {b}（区域名称），{c}（合并数值）, {d}（无）
              formatter: '地区：{b}<br/> 累计确诊：{c} '
            },
            // 右侧工具栏
            toolbox: {
              show: true,
              orient: 'vertical',
              left: 'right',
              top: 'center',
              feature: {
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {}
              }
            },
            // 视觉映射组件
            visualMap: {
              min: 0,
              max: 500,
              left: '2%',
              top: '30%',
              text: ['高','低'],
              calculable : true,
              hoverLink: true,
              inRange: {
                color: [
                  '#00ff8f',
                  '#389d32',
                  '#367933',
                  '#eee0a9',
                  '#dde567',
                  '#f1f107',
                  '#ff9002',
                  '#d06c07',
                  '#f46d43',
                  '#d73027',
                  '#a50026'
                ]
              },
            },
            series : [
              {
                name: '',
                type: 'map',
                map: 'china',
                // 鼠标缩放和平移漫游
                roam: true,
                itemStyle: {
                  normal:{
                    borderColor: 'rgba(0, 0, 0, 0.2)'
                  },
                  emphasis:{
                    shadowOffsetX: 0,
                    shadowOffsetY: 0,
                    shadowBlur: 20,
                    borderWidth: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                  }
                },
                showLegendSymbol: true,
                label: {
                  show: true,
                  emphasis: {
                    show: true
                  }
                },
                // 数据
                data: this.datas,
                // 自定义名称映射
                nameMap: {
                  '香港特别行政区': '香港',
                  '澳门特别行政区': '澳门'
                }
              }
            ],
          })
      )
      option && chart.setOption(option);
      /*
      var that = this;
      chart.on('timelinechanged',function(timeLineIndx){
        console.log(timeLineIndx);
        that.getdata();
        option.data = this.datas;
        chart.setOption(option);  
    })
    */
  },

      drawMap(){
      //var that = this; 
      var chart = this.$echarts.init(this.$refs.map)
      chart.on('timelinechanged',function(timeLineIndx){
        console.log(timeLineIndx);
        var option = this.chart.getOption();
        this.getdata();
        option.data = this.datas;
        chart.setOption(option);  
    })
    },
  
  },

  mounted() {
    let chartDom = this.$refs.map
    let chart
    chart = this.$echarts.init(chartDom)     
  
    // 注册地图
    this.$echarts.registerMap('china', chinaJson)

    this.getdata();
    this.MapInit(chart);

    this.timer = setInterval(this.drawMap,2000);
    //clearInterval(this.timer);
    //this.MapInit();
  },
  
  beforeDestroy(){
    clearInterval(this.timer)
  }
  
}
</script>

<style scoped>

</style>
