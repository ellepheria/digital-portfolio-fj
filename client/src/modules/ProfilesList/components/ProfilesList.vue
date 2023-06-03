<template>
<profile-card
  v-for="card in profilesList"
  :name="card['name']"
  :about="card['about']"
  :cover_path="card['images'].cover_path"
  :profile_picture_path="card['images'].profile_picture_path"
  :type_of_activity="card['type_of_activity']"
>

</profile-card>
</template>

<script>
import ProfileCard from "@/UI/ProfileCard/components/ProfileCard.vue";

export default {
  name: "ProfilesList",
  components: {ProfileCard},
  props: {
    profilesList: [],
  }
}
</script>

<style scoped>

</style>