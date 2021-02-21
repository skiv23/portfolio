<template>
  <div id="app">
    <div class="cv" v-if="!download">
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
    <div class="cv" v-else>
      <div class="cv-right">
        <SlideDownload/>
      </div>
    </div>
  </div>
</template>

<script>
  import InfoSidebar from './components/InfoSidebar.vue'
  import MenuNav from './components/MenuNav.vue'
  import ArrowNav from './components/ArrowNav.vue'
  import SlideDownload from './components/SlideDownload.vue'

  export default {
    name: 'App',
    components: {
      InfoSidebar,
      MenuNav,
      ArrowNav,
      SlideDownload
    },
    data () {
      return {
        transitionName: ''
      }
    },
    computed: {
      download() {
        const enabled = this.$route.query.download !== undefined;
        const html = document.getElementsByTagName('html')[0]
        if (enabled) {
          html.classList.add('download')
        } else {
          html.classList.remove('download')
        }
        return enabled
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
