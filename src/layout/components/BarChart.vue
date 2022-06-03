<template>
    <div id="bar" style="height: 100%; width: 100%"></div>
  
</template>

<script>
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

export default {
  name: 'BarChart',
  data() {
      return {  
        bardata: [],
        top:[],
        box_office:[]
      }
  },
  methods: {
      getdata() {
        var url = 'http://localhost:8080/data/bardata.json'
        axios.get(url)
          .then((res) => {
            this.bardata = res.data.bardata;
            //console.log(this.bardata)
            for (var i = 0; i < this.bardata[0].top.length; i++){
                this.top.push(this.bardata[0].top[i]);
                this.box_office.push(this.bardata[0].box_office[i])
                }
          })
          .catch((error) => {
            console.log(error);
          })
      },

    drawBar(myBar){

        var that = this;
        //图表的配置项和数据
        var option = {             
                title: {
                    text: '当月票房Top3电影',
                },
                tooltip: {
                  trigger: 'axis',
                  formatter:'电影名称:{b}<br/> 票房:{c}(单位：元)',
                  axisPointer: {
                    type: 'shadow'
                  }
                },
  
                grid: {
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis: {
                  type: 'value',
                  boundaryGap: [0, 0.01]
                },
                yAxis: {
                  type: 'category',
                  axisLabel: {        
                    textStyle: {
                      fontSize: '12',
                      fontWeight: 'bold'
                    }
                  },
                  data:that.top,
                },
              series: [
                {
                  type: 'bar',
                  data: that.box_office,
                  itemStyle: {
                  borderRadius: [0,50,50, 0],
                  color: {
                    type: 'linear',
                    x: 0,
                    y: 0,
                    x2: 1,
                    y2: 0,
                    colorStops: [{
                    offset: 0, color: '#5050ee' // 0% 处的颜色
                    }, 
                    {
                    offset: 1, color: '#ab6ee5' // 100% 处的颜色
                    }],
                    global: false // 缺省为 false
                  },
                }
              }],
            };
        
        //使用刚指定的配置项和数据显示图表。
        setTimeout(()=>{
        option && myBar.setOption(option,true);
      },100) 

        VueEvent.on('timelinechanged',currentIndex =>{
            //console.log(currentIndex);
            that.top = []
            that.box_office = []
            for (var i = 0; i < that.bardata[currentIndex].top.length; i++){
                //console.log(i)
                that.top.push(that.bardata[currentIndex].top[i]);
                that.box_office.push(that.bardata[currentIndex].box_office[i]);
            }
            setTimeout(()=>{
                myBar.setOption({
                  yAxis: {
                    data:that.top,
                },
                  series: [{
                  data: that.box_office,
                  },
                  ]
                })
            },100) 
  
       })
    },
  },
    created(){
        this.getdata();
    },

    mounted(){
        var myBar = this.$echarts.init(document.getElementById('bar'));
        this.drawBar(myBar);
  },
};


</script>

<style scoped>

</style>

