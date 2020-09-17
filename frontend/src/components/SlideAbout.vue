<template>
  <section class="cv-details-section about">
    <div class="page-title">
      <h2>About Me</h2>
    </div>
    <div class="cv-details-section-content">
      <!-- Personal Information -->
      <div class="row">
        <div class="cv-details-section-content-left">
          <p>Proin volutpat mauris ac pellentesque pharetra. Suspendisse congue elit vel odio suscipit, sit amet tempor
            nisl imperdiet. Quisque ex justo, faucibus ut mi in, condimentum finibus dolor. Aliquam vitae hendrerit
            dolor, eget imperdiet mauris. Maecenas et ante id ipsum condimentum dictum et vel massa. Ut in imperdiet
            dolor, vel consectetur dui.</p>
        </div>

        <div class="cv-details-section-content-right">
          <div class="info-list">
            <ul>
              <li>
                <span class="title">Age</span>
                <span class="value">{{ new Date().getFullYear() - 1994 }}</span>
              </li>

              <li>
                <span class="title">Residence</span>
                <span class="value">Belarus</span>
              </li>

              <li>
                <span class="title">City</span>
                <span class="value">Minsk</span>
              </li>

              <li>
                <span class="title">Email</span>
                <span class="value">
                  <a href="mailto:sergey.bondar.dev@gmail.com">sergey.bondar.dev@gmail.com</a>
                </span>
              </li>

              <li>
                <span class="title">Telegram</span>
                <span class="value">
                  <a href="https://telegram.me/sbondar_tg">sbondar_tg</a>
                </span>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <!-- End of Personal Information -->

      <div class="white-space-50"></div>

      <!-- Services -->
      <div class="row">
        <div>
          <div class="block-title">
            <h3>What I Do</h3>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="cv-details-section-content-left">
          <div class="what-i-do">
            <div class="what-i-do-icon">
              <font-awesome-icon icon="cogs"/>
            </div>
            <div class="what-i-do-text">
              <h4>Backend</h4>
              <p>Pellentesque pellentesque, ipsum sit amet auctor accumsan, odio tortor bibendum massa, sit amet
                ultricies ex lectus scelerisque nibh. Ut non sodales.</p>
            </div>
          </div>
        </div>

        <div class="cv-details-section-content-right">
          <div class="what-i-do">
            <div class="what-i-do-icon">
              <font-awesome-icon icon="laptop-code"/>
            </div>
            <div class="what-i-do-text">
              <h4>Frontend</h4>
              <p>Pellentesque pellentesque, ipsum sit amet auctor accumsan, odio tortor bibendum massa, sit amet
                ultricies ex lectus scelerisque nibh. Ut non sodales.</p>
            </div>
          </div>
        </div>
      </div>
      <!-- End of Services -->

    </div>
  </section>
</template>

<script>
  export default {
    name: "About"
  }
</script>

<style scoped>

</style>
