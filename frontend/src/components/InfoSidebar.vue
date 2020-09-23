<template>
  <div class="cv-left">
    <div class="cv-photo">
      <img src="../assets/photo.png" alt="photo">
    </div>
    <div class="cv-titles">
      <h2>Sergey Bondar</h2>
      <h4>Web developer</h4>
    </div>
    <div class="cv-social-links">
      <ul>
        <li>
          <a href="https://linkedin.com/in/sergey-bondar-47960690" target="_blank">
            <font-awesome-icon :icon="['fab', 'linkedin-in']"/>
          </a>
        </li>
        <li>
          <a href="mailto:sergey.bondar.dev@gmail.com">
            <font-awesome-icon icon="envelope"/>
          </a>
        </li>
        <li>
          <a href="https://telegram.me/sbondar_tg">
            <font-awesome-icon icon="paper-plane"/>
          </a>
        </li>
      </ul>
    </div>
    <div class="cv-header-buttons">
      <a href="#" target="_blank" class="btn btn-primary">Download CV</a>
      <theme-switch></theme-switch>
    </div>
  </div>
</template>

<script>
  import ThemeSwitch from './ThemeSwitch.vue'
  export default {
    name: "InfoSidebar",
    components: {
      ThemeSwitch
    }
  }
</script>

<style scoped>

</style>
