<template>
  <div class="project-list">
      <profile-card
          class="project-card"
          v-for="card in profilesList"
          :key="card.username"
          :name="card['name']"
          :about="card['about']"
          :cover_path="card['images'].cover_path"
          :profile_picture_path="card['images'].profile_picture_path"
          :type_of_activity="card['type_of_activity']"
          :username="card.username"
      >
      </profile-card>
  </div>
</template>

<script>
import ProfileCard from "@/UI/ProfileCard/components/ProfileCard.vue";

export default {
  name: "ProfilesList",
  components: {ProfileCard},
  props: {
    profilesList: Array,
  }
}
</script>

<style scoped>
.project-list {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-between;
  flex-wrap: wrap;
}
.project-card {
  flex: 0 0 33.333333%;
  width: 450px;
}
</style>