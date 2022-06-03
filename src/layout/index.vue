<template>
  <div class="container">
    <!-- ---HEADER--- -->
    <header>
      <Header/>
    </header>
    <Main/>
  </div>
</template>

<script>
import Header from "@/layout/components/Header"
import Main from "@/layout/components/Main"

export default {
  name: "index",
  components: {
    Header,
    Main
  }
}
</script>

<style scoped>

</style>
