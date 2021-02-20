<template>
  <div class="arrows-nav">
    <div class="arrow arrow-left" @click="prevScreen">
      <i>&lt;</i>
    </div>
    <div class="arrow arrow-right" @click="nextScreen">
      <i>&gt;</i>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ArrowNav",
    data() {
      return {
        paths: this.$router.options.routes.map(route => {
          return route.path
        })
      }
    },
    computed: {
      currentRouteIndex() {
        return this.paths.indexOf(this.$route.path)
      },
      nextRouteIndex() {
        return this.currentRouteIndex + 1 < this.paths.length ? this.currentRouteIndex + 1 : 0
      },
      prevRouteIndex() {
        return this.currentRouteIndex - 1 > -1 ? this.currentRouteIndex - 1 : this.paths.length - 1
      }
    },
    methods: {
      nextScreen() {
        this.$router.push(this.paths[this.nextRouteIndex])
      },
      prevScreen() {
        this.$router.push(this.paths[this.prevRouteIndex])

      }
    }
  }
</script>

<style scoped>

</style>
