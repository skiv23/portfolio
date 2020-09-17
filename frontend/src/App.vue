<template>
  <div id="app">
    <div class="cv">
      <MenuNav/>
      <ArrowNav/>
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
  import MenuNav from './components/MenuNav.vue'
  import ArrowNav from './components/ArrowNav.vue'

  export default {
    name: 'App',
    components: {
      InfoSidebar,
      MenuNav,
      ArrowNav,
    },
    data () {
      return {
        transitionName: ''
      }
    },
    watch: {
      '$route'(to, from) {
        const paths = this.$router.options.routes.map(route => {
            return route.path
        })
        const toDepth = paths.indexOf(to.path)
        const fromDepth = paths.indexOf(from.path)
        this.transitionName = toDepth < fromDepth ? 'moveDown' : 'moveUp'
      }
    }
  }
</script>

<style lang="scss">
  @import 'src/assets/scss/styles.scss';
</style>
