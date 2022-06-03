<template>
  <div>
    <h1>可视化小分队</h1>
    <div class="time" ref="time">
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  methods: {
    showTime() {
      // 获取当前时间
      let t = null
      t = setTimeout(time, 1000)
      // 显示规范化 
      function addZero(i){
        if (i<10) {
          i = '0' + i
        }
        return i
      }

      function time() {
        clearTimeout(t)
        let dt = new Date()
      
        let year = dt.getFullYear()
        let month = dt.getMonth()
        let day = dt.getDate()
        let hours = dt.getHours()
        let min = addZero(dt.getMinutes())
        let sec = addZero(dt.getSeconds())

        document.querySelector('.time').innerHTML = year + '年' + (month + 1) + '月' + day + '日'
            + hours + ':' + min + ':' + sec
        t = setTimeout(time, 1000)
      }
    }
  },
  mounted() {
    this.showTime()
  }
}
</script>

<style scoped>

</style>
