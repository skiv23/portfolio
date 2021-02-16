<template>
  <section class="cv-details-section about">
    <div class="page-title">
      <h2>About Me</h2>
    </div>
    <div class="cv-details-section-content">
      <div class="row">
        <div class="cv-details-section-content-left">
          <p>{{ about.description }}</p>
        </div>

        <div class="cv-details-section-content-right">
          <div class="info-list">
            <ul>
              <li v-for="infoEntry in about.info_entries" :key="infoEntry.id">
                <span class="title">{{ infoEntry.title }}</span>
                <span class="value" v-html="infoEntry.value_display"></span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="white-space-50"></div>

      <div class="row">
        <div>
          <div class="block-title">
            <h3>What I Do</h3>
          </div>
        </div>
      </div>

      <div class="row row-wrap">
        <div :class="[index % 2 === 0 ? 'cv-details-section-content-left': 'cv-details-section-content-right']"
             v-for="(whatIDo, index) in whatIDoList" :key="whatIDo.id">
          <div class="what-i-do">
            <div class="what-i-do-icon" v-if="whatIDo.icon">
              <font-awesome-icon :icon="whatIDo.icon"/>
            </div>
            <div class="what-i-do-text">
              <h4>{{ whatIDo.name }}</h4>
              <p>{{ whatIDo.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import AboutDataService from '../services/AboutDataService'
  import WhatIDoDataService from '../services/WhatIDoDataService'

  export default {
    name: "About",
    data() {
      return {
        about: {},
        whatIDoList: []
      }
    },
    mounted() {
      AboutDataService.get()
        .then(response => {
          this.about = response.data
        })
      WhatIDoDataService.getAll()
        .then(response => {
          this.whatIDoList = response.data
        })
    }
  }
</script>

<style scoped>

</style>
