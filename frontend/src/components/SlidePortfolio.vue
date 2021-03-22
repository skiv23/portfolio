<template>
  <section class="cv-details-section portfolio">
    <div class="page-title">
      <h2>Portfolio</h2>
    </div>
    <div class="cv-details-section-content">
      <div class="row row-wrap">
        <div class="portfolio-item" @click="openModal(project)" v-for="project in projects" :key="project.id">
          <div class="portfolio-item-img">
            <img v-if="download" :src="project.primary_image_url" crossorigin="anonymous" :alt="project.name" :title="project.name">
            <img v-else :src="project.thumbnail_image_url" crossorigin="anonymous" :alt="project.name" :title="project.name">
          </div>

          <h4 class="name">{{ project.name }}</h4>
          <div class="portfolio-block" v-if="download">
            <ProjectDescription :project="project"/>
          </div>
        </div>
      </div>
    </div>
    <portfolio-modal v-if="isModalOpen" :project="modalProject" @close="closeModal()"></portfolio-modal>
  </section>
</template>

<script>
  import PortfolioModal from './PortfolioModal.vue';
  import ProjectDataService from '../services/ProjectDataService';
  import ProjectDescription from './ProjectDescription.vue';

  export default {
    name: "Portfolio",
    components: {
      PortfolioModal,
      ProjectDescription
    },
    data() {
      return {
        isModalOpen: false,
        projects: [],
        modalProject: null
      }
    },
    props: {
      download: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      openModal(project) {
        this.modalProject = project
        this.isModalOpen = true
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
