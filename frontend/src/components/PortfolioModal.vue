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
          <h1>Portfolio Project 1</h1>
        </div>

        <div class="row">
          <div class="portfolio-block portfolio-block-left">
            <vue-flux
              :options="vfOptions"
              :images="vfImages"
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
                <li><p><font-awesome-icon icon="user"/> Alex Smith</p></li>
                <li><p><font-awesome-icon icon="globe"/> <a href="#" target="_blank">www.project-site.com</a></p></li>
                <li><p><font-awesome-icon icon="calendar"/> 25 december, 2016</p></li>
              </ul>

              <p class="text-justify">Aliquam euismod aliquam massa, quis eleifend dui sodales vitae. Interdum et
                malesuada fames ac ante ipsum primis in faucibus.</p>
              <div class="tags-block">
                <div class="block-title">
                  <h3>Technology</h3>
                </div>
                <ul class="tags">
                  <li><a>HTML5</a></li>
                  <li><a>CSS3</a></li>
                  <li><a>jQuery</a></li>
                  <li><a>Ajax</a></li>
                  <li><a>PHP5</a></li>
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
    }
  }
</script>

<style scoped>

</style>
