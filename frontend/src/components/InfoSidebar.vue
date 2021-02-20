<template>
  <div>
    <div class="menu-toggle" @click="toggleSidebar" :class="{ open: sideBarOpen }">
      <span></span>
      <span></span>
      <span></span>
    </div>
    <div class="cv-left" :class="{ open: sideBarOpen }">
      <div class="cv-photo">
        <img src="../assets/photo.png" alt="photo">
      </div>
      <div class="cv-titles">
        <h2>{{ nameTitle }}</h2>
        <h4>{{ roleTitle }}</h4>
      </div>
      <div class="cv-social-links">
        <ul>
          <li v-for="contact in contacts" :key="contact.id">
            <a v-if="contact.url" :href="contact.url" target="_blank">
              <font-awesome-icon :icon="JSON.parse(contact.icon)"/>
            </a>
          </li>
        </ul>
      </div>
      <div class="cv-mobile-menu">
        <MenuNav :use-icons="false"/>
      </div>
      <div class="cv-header-buttons">
        <a href="#" target="_blank" class="btn btn-primary">Download CV</a>
        <theme-switch></theme-switch>
      </div>
    </div>
  </div>
</template>

<script>
  import ThemeSwitch from './ThemeSwitch.vue'
  import TitleDataService from '../services/TitleDataService'
  import ContactDataService from '../services/ContactDataService'
  import MenuNav from './MenuNav.vue'

  export default {
    name: "InfoSidebar",
    data() {
      return {
        nameTitle: '',
        roleTitle: '',
        contacts: [],
        sideBarOpen: false
      }
    },
    components: {
      ThemeSwitch,
      MenuNav
    },
    mounted() {
      TitleDataService.getAll()
        .then(response => {
          response.data.forEach((title) => {
            if (title.type === 1) {
              this.nameTitle = title.text
            } else if (title.type === 2) {
              this.roleTitle = title.text
            }
          })
        })
      ContactDataService.filterByComponent('sidebar')
        .then(response => {
          this.contacts = response.data;
        })
    },
    methods: {
      toggleSidebar() {
        this.sideBarOpen = !this.sideBarOpen
      }
    }
  }
</script>

<style scoped>

</style>
