<template>
    <div style="height: 100%; width: 100%" ref="map">
    </div>
</template>

<script> 
import chinaJson from '@/assets/china.json'
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

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
  
        //this.getdata();
        // 注册地图
        this.$echarts.registerMap('china', chinaJson)
      
        var option = {
          // 引入时间轴
          timeline:{
            x:100,
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

          data: ['2020.1','2020.2','2020.3','2020.4','2020.5','2020.6','2020.7','2020.8','2020.9','2020.10',
          '2020.11','2020.12','2021.1','2021.2','2021.3','2021.4','2021.5','2021.6','2021.7','2021.8','2021.9',
          '2021.10','2021.11','2021.12','2022.1','2022.2','2022.3'],
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
                  },  
                },

                data: this.datas,

                // 自定义名称映射
                nameMap: {
                  '香港特别行政区': '香港',
                  '澳门特别行政区': '澳门'
                }
              }
            ],
          }

      // 更新数据
      setTimeout(()=>{
        option && chart.setOption(option,true);
      },100) 

      // 检测时间轴事件变化
      var that = this;
      chart.on('timelinechanged',function(timeLineIndx){
        //console.log(timeLineIndx);
        var res = timeLineIndx.currentIndex;
        that.getdata();
        setTimeout(()=>{
          chart.setOption(option);
        },100)
        VueEvent.emit('timelinechanged',res)
        //chart.setOption(option);  
    })
  },

    handleInitail(timeLineIndex){
      this.$bus.$on('TimelineChange',timeLineIndex)
    }

  },

  created(){
    this.getdata();
  },

  mounted() {
     // 初始化echarts实例
    let chartDom = this.$refs.map
    let chart = this.$echarts.init(chartDom) 
    this.MapInit(chart);  
  },
}
</script>

<style scoped>

</style>
