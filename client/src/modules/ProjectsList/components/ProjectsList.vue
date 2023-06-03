<template>
  <project-card
      v-for="project in projectsList"
      :number="String(project['id'])"
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
    projectsList: [],
  }
}
</script>

<style scoped>

</style>