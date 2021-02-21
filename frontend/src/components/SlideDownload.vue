<template>
  <div class="cv-right-container">
    <ThemeSwitch/>
    <SlideHome/>
    <SlideAbout/>
    <SlideCV/>
    <SlidePortfolio :download="true"/>
  </div>
</template>

<script>
  import ThemeSwitch from "./ThemeSwitch.vue";
  import SlideHome from "./SlideHome.vue";
  import SlideAbout from "./SlideAbout.vue";
  import SlideCV from "./SlideCV.vue";
  import SlidePortfolio from "./SlidePortfolio.vue";
  import html2pdf from "html2pdf.js"

  export default {
    name: "SlideDownload",
    components: {
      ThemeSwitch,
      SlideHome,
      SlideAbout,
      SlideCV,
      SlidePortfolio,
    },
    mounted() {
      setTimeout(() =>{
        var element = document.getElementsByTagName('html')[0];
        html2pdf().set({
          filename: 'SergeyBondar.pdf',
          pagebreak: { after: '.cv-details-section' },
          // fix for svg images: https://github.com/eKoopmans/html2pdf.js/issues/185#issuecomment-455869320
          html2canvas: {
            useCORS: true,
            onclone: (element) => {
              const svgElements = Array.from(element.querySelectorAll('svg'));
              svgElements.forEach(s => {
                const bBox = s.getBBox();
                s.setAttribute("x", bBox.x);
                s.setAttribute("y", bBox.y);
                s.setAttribute("width", bBox.width);
                s.setAttribute("height", bBox.height);
              })
            }
          }
        }).from(element).save();
      }, 500)

    }
  }
</script>

<style scoped>
</style>
