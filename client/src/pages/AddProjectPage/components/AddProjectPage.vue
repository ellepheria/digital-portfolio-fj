<template>
  <Header></Header>
  <div class="form-container">
    <form @submit.prevent="addProject" class="form">
      <input
          v-model="title"
          class="title"
          type="text">
      <input
          v-model="shortDescription"
          type="text"
          class="short-description">
      <input
          v-model="description"
          type="text"
          class="description">
      <RedButton>Назад</RedButton>
      <BlueButton
          type="submit">Добавить</BlueButton>
    </form>
  </div>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import RedButton from "@/UI/Buttons/RedButton/RedButton.vue";
import BlueButton from "@/UI/Buttons/BlueButton/BlueButton.vue";
import $http, {baseURI} from "@/api";
import {getUsername} from "@/helpers";

export default {
  name: "AddProjectPage",
  components: {BlueButton, RedButton, Footer, Header},
  data() {
    return {
      title: '',
      shortDescription: '',
      description: '',
      images: [],
      added_links: {},
    };
  },
  methods: {
    async addProject() {
      let response;
      const url = baseURI + 'create_project';
      const payload = {
        title: this.title,
        short_description: this.shortDescription,
        description: this.description,
        added_links: [],
      }
      await $http.post(url, payload)
          .then(res => response = res);
      console.log(response);
    },
  },
  computed: {},
  created() {
    this.title = 'Project';
  },
}
</script>

<style scoped>

</style>