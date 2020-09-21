<template>
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
    <router-link :to="{ name: 'cv' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="graduation-cap"/>
        </a>
      </li>
    </router-link>
    <router-link :to="{ name: 'portfolio' }" v-slot="{ href, route, navigate, isActive, isExactActive }">
      <li>
        <a :class="{ active: isExactActive }" :href="href" @click="navigate">
          <font-awesome-icon icon="briefcase"/>
        </a>
      </li>
    </router-link>
  </ul>
</template>

<script>
  export default {
    name: "MenuNav"
  }
</script>

<style scoped>

</style>
