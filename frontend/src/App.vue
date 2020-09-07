<template>
  <div id="app">
    <div class="cv">
      <div class="cv-left">
        <div class="cv-photo">
          <img src="./assets/photo.png" alt="photo">
        </div>
        <div class="cv-titles">
          <h2>Sergey Bondar</h2>
          <h4>Web developer</h4>
        </div>
        <div class="cv-social-links">
          <ul>
            <li><a href="#" target="_blank">
              <font-awesome-icon :icon="['fab', 'linkedin-in']"/>
            </a></li>
          </ul>
        </div>
      </div>
      <div class="cv-right">
        <div class="cv-right-container">
          <SlideHome/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import SlideHome from './components/SlideHome.vue'

  export default {
    name: 'App',
    components: {
      SlideHome
    }
  }
</script>

<style lang="scss">
  @import 'src/assets/scss/styles.scss';
</style>
