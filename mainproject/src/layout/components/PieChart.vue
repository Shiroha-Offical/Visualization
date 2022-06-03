<template>
    <div id="pie" style="height: 100%; width: 100%"></div>
  
</template>

<script>
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

export default {
  name: 'PieChart',
  data() {
      return {  
        piedata: [],
        list:[]
      }
  },
  methods: {
      getdata() {
        var url = 'http://localhost:8080/data/piedata.json'
        axios.get(url)
          .then((res) => {
            this.piedata = res.data.piedata;
            console.log(this.piedata)
            for (var i = 0; i < this.piedata[0].list.length; i++){
                this.list.push(this.piedata[0].list[i])
                }
          })
          .catch((error) => {
            console.log(error);
          })
      },

    drawPie(myPie){

        var that = this;
        //图表的配置项和数据
        var option = {
          title: {
            text: '当月各类型电影上座率'
          },
          tooltip: {
            trigger: 'item'
          },
           feature: {
              mark: { show: true },
          },
          series: [
            {
              name: '类型及上座率',
              type: 'pie',
              radius: [50, 150],
              center: ['50%', '55%'],
              roseType: 'area',
              itemStyle: {
                borderRadius: 10
              },
              color: [
                '#405de6',
                '#5851db',
                '#833ab4',
                '#c13584',
                '#e1306c',
                '#fd1d1d',
                '#f56040',
                '#f77737',
                '#fcaf45',
                '#ffdc80',
                '#60ab59'
              ],
              labelLine: {
                lineStyle: {
                  borderRadius: 8
                },
                smooth: 0.2,
                length: 10,
                length2: 20
              },
              label: {
                fontWeight: 'bold',
                fontSize: 15
              },
              data: that.list
            }
          ]
};
        //使用刚指定的配置项和数据显示图表。
        setTimeout(()=>{
        option && myPie.setOption(option,true);
      },10) 

        VueEvent.on('timelinechanged',currentIndex =>{
            //console.log(currentIndex);
            that.list = []
            for (var i = 0; i < that.piedata[currentIndex].list.length; i++){
                //console.log(i)
                that.list.push(that.piedata[currentIndex].list[i]);
            }
            setTimeout(()=>{
                myPie.setOption({
                  series: [{
                  data: that.list,
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
        var myPie = this.$echarts.init(document.getElementById('pie'));
        this.drawPie(myPie);
  },
};


</script>

<style scoped>

</style>

