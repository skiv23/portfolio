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
  </ul>
</template>

<script>
  export default {
    name: "Menu"
  }
</script>

<style scoped>

</style>
