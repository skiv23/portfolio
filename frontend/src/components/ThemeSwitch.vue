<template>
  <div class="theme-switch" @click="switchColorTheme">
    <div class="switch" :class="currentTheme">
      <font-awesome-icon icon="sun" v-if="currentTheme === 'light'"></font-awesome-icon>
      <font-awesome-icon icon="moon" v-if="currentTheme === 'dark'"></font-awesome-icon>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ThemeSwitch",
    data() {
      return {
        currentTheme: this.getPreferredColorScheme()
      }
    },
    methods: {
      switchColorTheme() {
        let scheme
        if (this.currentTheme === 'light')
          scheme = 'dark'
        else {
          scheme = 'light'
        }
        this.setColorScheme(scheme)
      },
      setColorScheme(scheme) {
        this.currentTheme = scheme
        document.body.setAttribute('data-theme', scheme)
        localStorage.preferredColorScheme = scheme
      },
      getPreferredColorScheme() {
        if (localStorage.preferredColorScheme) {
          return localStorage.preferredColorScheme
        }
        if (window.matchMedia) {
          if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark'
          } else {
            return 'light'
          }
        }
        return 'light'
      }
    },
    mounted() {
      this.setColorScheme(this.getPreferredColorScheme())
    }
  }
</script>

<style scoped>

</style>
