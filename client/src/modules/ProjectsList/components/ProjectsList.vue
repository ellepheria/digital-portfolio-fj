<template>
  <project-card
      v-for="(project, index) in projectsList"
      :id="project.id"
      :key="project.id"
      :number="String(index + 1)"
      :short-description="project['short_description'] || 'null'"
      :title="project['title'] || 'null'"
      :cover_path="project['cover_path']">
  </project-card>
</template>

<script>
import ProjectCard from "@/UI/ProjectCard";
import {baseURI} from "@/api";

export default {
  name: "ProjectsList",
  methods: {
    baseURI() {
      return baseURI
    }
  },
  components: {ProjectCard},
  props: {
    projectsList: Array,
  }
}
</script>

<style scoped>

</style>