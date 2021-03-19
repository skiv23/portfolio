<template>
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
        <ul class="tags">
          <li v-for="skill in project.skills" :key="skill.id"><a>{{ skill.name }}</a></li>
        </ul>
      </div>

    </div>
</template>

<script>
  export default {
    name: "ProjectDescription",
    props: {
      project: Object
    }
  }
</script>

<style scoped>

</style>
