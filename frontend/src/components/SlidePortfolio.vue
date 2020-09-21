<template>
  <section class="cv-details-section curriculum-vitae">
    <div class="page-title">
      <h2>Portfolio</h2>
    </div>
    <div class="cv-details-section-content">
      <div class="row row-wrap">
        <div class="portfolio-item" @click="openModal()">
          <div class="portfolio-item-img">
            <img src="../assets/1.jpg" alt="SoundCloud Audio" title="">
            <a
              href="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/221650664&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
              class="lightbox mfp-iframe" title="SoundCloud Audio"></a>
          </div>

          <h4 class="name">SoundCloud Audio</h4>
        </div>
        <div class="portfolio-item">
          <div class="portfolio-item-img">
            <img src="../assets/1.jpg" alt="SoundCloud Audio" title="">
            <a
              href="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/221650664&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
              class="lightbox mfp-iframe" title="SoundCloud Audio"></a>
          </div>

          <h4 class="name">SoundCloud Audio</h4>
        </div>
        <div class="portfolio-item">
          <div class="portfolio-item-img">
            <img src="../assets/1.jpg" alt="SoundCloud Audio" title="">
            <a
              href="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/221650664&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
              class="lightbox mfp-iframe" title="SoundCloud Audio"></a>
          </div>

          <h4 class="name">SoundCloud Audio</h4>
        </div>
        <div class="portfolio-item">
          <div class="portfolio-item-img">
            <img src="../assets/1.jpg" alt="SoundCloud Audio" title="">
            <a
              href="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/221650664&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
              class="lightbox mfp-iframe" title="SoundCloud Audio"></a>
          </div>

          <h4 class="name">SoundCloud Audio</h4>
        </div>
        <div class="portfolio-item">
          <div class="portfolio-item-img">
            <img src="../assets/1.jpg" alt="SoundCloud Audio" title="">
            <a
              href="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/221650664&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
              class="lightbox mfp-iframe" title="SoundCloud Audio"></a>
          </div>

          <h4 class="name">SoundCloud Audio</h4>
        </div>
        <div class="portfolio-item">
          <div class="portfolio-item-img">
            <img src="../assets/1.jpg" alt="SoundCloud Audio" title="">
            <a
              href="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/221650664&amp;color=%23ff5500&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
              class="lightbox mfp-iframe" title="SoundCloud Audio"></a>
          </div>

          <h4 class="name">SoundCloud Audio</h4>
        </div>
      </div>
    </div>
    <portfolio-modal v-if="isModalOpen" @close="closeModal()"></portfolio-modal>
  </section>
</template>

<script>
  import PortfolioModal from './PortfolioModal.vue';
  export default {
    name: "Portfolio",
    components: {
      PortfolioModal
    },
    data() {
      return {
        isModalOpen: false
      }
    },
    methods: {
      openModal() {
        this.isModalOpen = true
      },
      closeModal() {
        this.isModalOpen = false
      }
    }
  }
</script>

<style scoped>

</style>
