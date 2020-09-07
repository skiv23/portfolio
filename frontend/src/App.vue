<template>
  <div id="app">
    <div class="cv">
      <Menu/>
      <InfoSidebar/>

      <div class="cv-right">
        <div class="cv-right-container">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import InfoSidebar from './components/InfoSidebar.vue'
  import Menu from './components/Menu.vue'

  export default {
    name: 'App',
    components: {
      InfoSidebar,
      Menu
    }
  }
</script>

<style lang="scss">
  @import 'src/assets/scss/styles.scss';
</style>
