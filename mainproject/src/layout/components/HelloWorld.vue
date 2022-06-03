<template>
    <div id="line" style="height: 100%; width: 100%"></div>
  
</template>

<script>
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

export default {
  name: 'HelloWorld',
  data() {
      return {  
        linedata: [],
        before_box_office:[],
        after_box_office:[],
        new_cases:[]

      }
  },
  methods: {
      getdata() {
        var url = 'http://localhost:8080/data/linedata.json'
        axios.get(url)
          .then((res) => {
            this.linedata = res.data.linedata;
            //console.log(this.linedata)
            for (var i = 0; i < this.linedata[0].new_cases.length; i++){
                this.before_box_office.push(this.linedata[0].before_box_office[i]);
                this.after_box_office.push(this.linedata[0].after_box_office[i]);
                this.new_cases.push(this.linedata[0].new_cases[i])
                }
          })
          .catch((error) => {
            console.log(error);
          })
      },

    drawLine(myLine){

        var that = this;
        //图表的配置项和数据
        var option = {         
                title: {
                    text: '疫情前后每日电影票房及当日新增确诊人数',
                },
                grid: {},
                xAxis: [
                    {
                        'type': 'category',//类目轴
                        'data': ['1日', '2日', '3日', '4日', '5日', '6日', '7日','8日', '9日', '10日', '11日', '12日', '13日', '14日','15日', '16日', '17日', '18日', '19日', '20日', '21日','22日', '23日', '24日', '25日', '26日','27日', '28日', '29日', '30日', '31日'],
                        axisPointer: {
                            type: 'shadow'
                        },
                        scale: true,            //脱离0值比例
                        boundaryGap: false           // 折线紧挨边缘
                    },
                ],
                yAxis: [
                    {
                        name:'当日票房',
                        'type': 'value',//数值轴
                        min: 0,
                        interval: 100000000,
                        axisLabel: {
                            formatter: '{value}元'
                        }
                    },
                    {
                        name:'当日新增确诊人数',
                        'type': 'value',
                        min: 0,
                        interval: 1000,
                        axisLabel: {
                            formatter: '{value}人'
                        }
                    }
                ],
                legend: {
                    data: ['疫情前每日票房', '疫情后每日票房', '当日新增确诊人数'],
                    right:20
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        crossStyle: {
                        color: '#999'
                        }
                    }
                },

                series: [
                    {name: '疫情前每日票房', type: 'bar',data: that.before_box_office},
                    {name: '疫情后每日票房', type: 'bar',data: that.after_box_office},
                    {name: '当日新增确诊人数', type: 'line',yAxisIndex: 1,data: that.new_cases}
                ]    
        }; 
 
        //使用刚指定的配置项和数据显示图表。
        setTimeout(()=>{
        option && myLine.setOption(option,true);
      },10)

       VueEvent.on('timelinechanged',currentIndex =>{
            //console.log(currentIndex);
            that.before_box_office = []
            that.after_box_office = []
            that.new_cases = [] 
            for (var i = 0; i < that.linedata[currentIndex].new_cases.length; i++){
                //console.log(i)
                that.before_box_office.push(that.linedata[currentIndex].before_box_office[i]);
                that.after_box_office.push(that.linedata[currentIndex].after_box_office[i]);
                that.new_cases.push(that.linedata[currentIndex].new_cases[i]);
            }
            setTimeout(()=>{
                myLine.setOption({
                    series:[
                        {name: '疫情前每日票房', type: 'bar',data: that.before_box_office},
                        {name: '疫情后每日票房', type: 'bar',data: that.after_box_office},
                        {name: '当日新增确诊人数', type: 'line',yAxisIndex: 1,data: that.new_cases}
                    ]
                });
            },100) 
       })
/*
       myLine.on('timelinechange',function(timeLineIndex){
            console.log(timeLineIndex.currentIndex);
            //console.log(timeLineIndex.currentIndex.type)
            that.before_box_office = []
            that.after_box_office = []
            that.new_cases = [] 
    
            for (var i = 0; i < that.linedata[timeLineIndex.currentIndex].new_cases.length; i++){
                that.before_box_office.push(that.linedata[timeLineIndex.currentIndex].before_box_office[i]);
                that.after_box_office.push(that.linedata[timeLineIndex.currentIndex].after_box_office[i]);
                that.new_cases.push(that.linedata[timeLineIndex.currentIndex].new_cases[i]);
            }
        }
       )
       
       
            //console.log(option.series)

            setTimeout(()=>{
                myLine.setOption({
                    series:[
                        {name: '疫情前每日票房', type: 'bar',data: that.before_box_office},
                        {name: '疫情后每日票房', type: 'bar',data: that.after_box_office},
                        {name: '当日新增确诊人数', type: 'line',yAxisIndex: 1,data: that.new_cases}
                    ]
                });
            },100) 
            */
        }
    },
  
    created(){
        this.getdata();
    },

    mounted(){
        var myLine = this.$echarts.init(document.getElementById('line'));
        this.drawLine(myLine);
  },
};


</script>

<style scoped>

</style>

