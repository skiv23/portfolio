<template>
  <div id="page-ajax-loaded" class="page-ajax-loaded animated animated-section-moveFromLeft">
    <div id="ajax-page" class="ajax-page-content">
      <div class="ajax-page-wrapper">
        <div class="ajax-page-nav">
          <div class="nav-item ajax-page-close-button">
            <a id="ajax-page-close-button" href="#" @click="$emit('close')">+</a>
          </div>
        </div>

        <div class="ajax-page-title">
          <h1>{{ project.name }}</h1>
        </div>

        <div class="row">
          <div class="portfolio-block portfolio-block-left">
            <vue-flux
              :options="vfOptions"
              :images="project.images"
              :transitions="vfTransitions"
              ref="slider"
            >
              <template v-slot:controls>
                <flux-controls/>
              </template>
            </vue-flux>
          </div>

          <div class="portfolio-block portfolio-block-right">
            <ProjectDescription :project="project"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {
   VueFlux,
   FluxControls,
  } from 'vue-flux';
  import ProjectDescription from './ProjectDescription.vue';

  export default {
    name: "PortfolioModal",
    components: {
      VueFlux,
      FluxControls,
      ProjectDescription
    },
    data() {
      return {
        vfOptions: {
          autohideTime: 0,
          autoPlay: false,
        },
        vfImages: this.project.images,
        vfTransitions: [{
          name: 'slide',
          options: {
            totalDuration: 500,
            easing: 'ease',
          }
        }],
      }
    },
    props: {
      project: Object
    }
  }
</script>

<style scoped>

</style>
