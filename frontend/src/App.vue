<template>
  <div id="app">
    <div class="cv">
      <ul class="menu">
        <router-link :to="{ name: 'home' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
          <li>
            <a :class="{ active: isExactActive }" :href="href" @click="navigate">
              <font-awesome-icon icon="home"/>
            </a>
          </li>
        </router-link>
        <router-link :to="{ name: 'about' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
          <li>
            <a :class="{ active: isExactActive }" :href="href" @click="navigate">
              <font-awesome-icon icon="user"/>
            </a>
          </li>
        </router-link>
      </ul>
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
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'App',
    components: {}
  }
</script>

<style lang="scss">
  @import 'src/assets/scss/styles.scss';
</style>
