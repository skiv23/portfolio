<template>
  <ul class="menu">
    <router-link :to="{ name: 'home' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="home" v-if="useIcons"/>
          <span v-else>Home</span>
        </a>
      </li>
    </router-link>
    <router-link :to="{ name: 'about' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="user" v-if="useIcons"/>
          <span v-else>About</span>
        </a>
      </li>
    </router-link>
    <router-link :to="{ name: 'cv' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="graduation-cap" v-if="useIcons"/>
          <span v-else>CV</span>
        </a>
      </li>
    </router-link>
    <router-link :to="{ name: 'portfolio' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="briefcase" v-if="useIcons"/>
          <span v-else>Portfolio</span>
        </a>
      </li>
    </router-link>
    <router-link :to="{ name: 'contact' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="envelope" v-if="useIcons"/>
          <span v-else>Contact</span>
        </a>
      </li>
    </router-link>
  </ul>
</template>

<script>
  export default {
    name: "MenuNav",
    props: {
      useIcons: {
        type: Boolean,
        default: true
      }
    }
  }
</script>

<style scoped>

</style>
