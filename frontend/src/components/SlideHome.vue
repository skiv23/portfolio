<template>
  <section class="cv-details-section">
    <div class="vertical-center">
      <div class="title-block">
        <h2>{{ nameTitle }}</h2>
        <h4>{{ roleTitle }}</h4>
        <h4>{{ techStackTitle }}</h4>
      </div>
    </div>
  </section>
</template>

<script>
  import TitleDataService from '../services/TitleDataService'

  export default {
    name: "Home",
    data() {
      return {
        nameTitle: '',
        roleTitle: '',
        techStackTitle: '',
      }
    },
    mounted() {
      TitleDataService.getAll()
        .then(response => {
          response.data.forEach((title) => {
            if (title.type === 1) {
              this.nameTitle = title.text
            } else if (title.type === 2) {
              this.roleTitle = title.text
            } else if (title.type === 3) {
              this.techStackTitle = title.text
            }
          })
        })
    }
  }
</script>

<style scoped>

</style>
