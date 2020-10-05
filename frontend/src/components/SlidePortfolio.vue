<template>
  <section class="cv-details-section portfolio">
    <div class="page-title">
      <h2>Portfolio</h2>
    </div>
    <div class="cv-details-section-content">
      <div class="row row-wrap">
        <div class="portfolio-item" @click="openModal(project.id)" v-for="project in projects" :key="project.id">
          <div class="portfolio-item-img">
            <img :src="project.primary_image_url" :alt="project.name" :title="project.name">
          </div>

          <h4 class="name">{{ project.name }}</h4>
        </div>
      </div>
    </div>
    <portfolio-modal v-if="isModalOpen" :project="modalProject" @close="closeModal()"></portfolio-modal>
  </section>
</template>

<script>
  import PortfolioModal from './PortfolioModal.vue';
  import ProjectDataService from '../services/ProjectDataService';
  export default {
    name: "Portfolio",
    components: {
      PortfolioModal
    },
    data() {
      return {
        isModalOpen: false,
        projects: [],
        modalProject: null
      }
    },
    methods: {
      openModal(id) {
        ProjectDataService.get(id)
          .then(response => {
            this.modalProject = response.data
            this.isModalOpen = true
          })
      },
      closeModal() {
        this.modalProject = null
        this.isModalOpen = false
      }
    },
    mounted() {
      ProjectDataService.getAll()
        .then(response => {
          this.projects = response.data
        })
    }
  }
</script>

<style scoped>

</style>
