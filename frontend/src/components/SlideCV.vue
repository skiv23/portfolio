<template>
  <section class="cv-details-section curriculum-vitae">
    <div class="page-title">
      <h2>CV</h2>
    </div>
    <div class="cv-details-section-content">
      <div class="row">
        <div class="cv-details-section-content-left">
          <div class="timeline-wrapper" v-for="(timeline, index) in timelines" :key="timeline.id">
            <div class="block-title">
              <h3>{{ timeline.name }}</h3>
            </div>

            <div class="timeline clearfix">
              <div class="timeline-item clearfix"
                   v-for="timelineEntry in timeline.entries" :key="timelineEntry.id">
                <div class="left-part">
                  <h5 class="item-period">{{ timelineEntry.years }}</h5>
                  <span class="item-company">{{ timelineEntry.place }}</span>
                </div>
                <div class="divider"></div>
                <div class="right-part">
                  <h4 class="item-title">{{ timelineEntry.name }}</h4>
                  <p>{{ timelineEntry.description }}</p>
                </div>
              </div>
            </div>
            <div class="white-space-50" v-if="index != timelines.length - 1"></div>
          </div>
        </div>

        <div class="cv-details-section-content-right">
          <div class="block-title">
            <h3>Main Skills</h3>
          </div>
          <div class="skills">
            <div class="skill-wrapper" v-for="skill in mainSkills" :key="skill.id">
              <div class="skill clearfix">
                <h4>{{ skill.name }}</h4>
                <div class="skill-value">{{ skill.percent }}%</div>
              </div>
              <div class="skill-container">
                <div class="skill-percentage" :style="{ width: skill.percent + '%' }"></div>
              </div>
            </div>
          </div>

          <div class="block-title" v-if="secondarySkills.length">
            <h3>Secondary Skills</h3>
          </div>
          <ul class="knowledges" v-if="secondarySkills.length">
            <li v-for="skill in secondarySkills" :key="skill.id">{{ skill.name }}</li>
          </ul>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
  import SkillDataService from '../services/SkillDataService'
  import TimelineDataService from '../services/TimelineDataService'

  export default {
    name: "About",
    data() {
      return {
        mainSkills: [],
        secondarySkills: [],
        timelines: []
      }
    },
    mounted() {
      SkillDataService.getAll()
        .then(response => {
          response.data.forEach(skill => {
            if (skill.is_secondary) {
              this.secondarySkills.push(skill)
            } else {
              this.mainSkills.push(skill)
            }
          })
        });
      TimelineDataService.getAll()
        .then(response => {
          this.timelines = response.data
        })
    }
  }
</script>

<style scoped>

</style>
