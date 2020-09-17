<template>
  <div id="app">
    <div class="cv">
      <Menu/>
      <InfoSidebar/>

      <div class="cv-right">
        <div class="cv-right-container">
          <transition :name="transitionName">
          <router-view></router-view>
            </transition>
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
    },
    data () {
      return {
        transitionName: ''
      }
    },
    watch: {
      '$route'(to, from) {
        let paths = ['/', '/about']
        const toDepth = paths.indexOf(to.path)
        const fromDepth = paths.indexOf(from.path)
        console.log(to, from, toDepth, fromDepth)
        this.transitionName = toDepth < fromDepth ? 'moveDown' : 'moveUp'
      }
    }
  }
</script>

<style lang="scss">
  @import 'src/assets/scss/styles.scss';
</style>
