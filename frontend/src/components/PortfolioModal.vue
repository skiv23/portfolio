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
            <div class="project-description">
              <div class="block-title">
                <h3>Description</h3>
              </div>
              <ul class="project-general-info">
                <li v-if="project.url">
                  <p>
                    <font-awesome-icon icon="globe"/> <a :href="project.url" target="_blank">{{ project.url }}</a>
                  </p>
                </li>
              </ul>

              <p class="text-justify">{{ project.description }}</p>
              <div class="tags-block">
                <div class="block-title">
                  <h3>Technology</h3>
                </div>
                <ul class="tags" >
                  <li v-for="tag in project.tags" :key="tag.id"><a>{{ tag.name }}</a></li>
                </ul>
              </div>

            </div>
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

  export default {
    name: "PortfolioModal",
    components: {
      VueFlux,
      FluxControls,
    },
    data() {
      return {
        vfOptions: {
          autohideTime: 0,
          autoPlay: false,
        },
        vfImages: [require('@/assets/1.jpg'), require('@/assets/2.jpg')],
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
