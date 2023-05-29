<template>
  <project-card
      v-for="project in projectsList"
      :title="project.title"
      :short-description="project.short_description"
      :id="project.id">
  </project-card>
</template>

<script>
import ProjectCard from "@/UI/ProjectCard";

export default {
  name: "ProjectsList",
  components: {ProjectCard},
  props: {
    projectsList: [
      {
        title: 'title',
        short_description: 'short_description',
        id: 1,
      }
    ],
  }
}
</script>

<style scoped>

</style>