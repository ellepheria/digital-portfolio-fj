<template>
  <Header></Header>
  <div
      v-if="!userIsOwner"
      class="access-denied"
  >Ошибка доступа: нельзя изменить чужой проект
  </div>

  <div class="main-container" v-if="userIsOwner">
    <div class="project-data-container">
      <div class="first-block">
        <div class="data-container">
          <div class="title">
            {{ title }}
          </div>
          <div class="short-description">
            {{ short_description }}
          </div>
        </div>
        <div class="cover-container"></div>
      </div>
      <div class="second-block">
        <div class="description">
          {{ description }}
        </div>
      </div>
      <div class="third-block">
        <div class="slider-container">
          Добавленные фотографии проекта
          <slider></slider>
          <BlueButton>
            Добавить фотографии проекта
          </BlueButton>
        </div>
        <div class="links">
          {{ added_links }}
          <div class="buttons">
            <RedButton class="cancel-button" @clicked="getProjectData">
              Отмена
            </RedButton>
            <BlueButton class="save-button" @clicked="saveProjectData">
              Сохранить
            </BlueButton>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import $http, {baseURI} from "@/api";
import {getUsername} from "@/helpers";
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import RedButton from "@/UI/Buttons/RedButton/RedButton.vue";
import BlueButton from "@/UI/Buttons/BlueButton/BlueButton.vue";
import Slider from "@/modules/Slider/components/Slider.vue";

export default {
  name: "ProjectEditPage",
  components: {Slider, BlueButton, RedButton, Footer, Header},
  data() {
    return {
      title: '',
      short_description: '',
      description: '',
      added_links: '',
      images: [],
      cover_path: '',
      userIsOwner: false,
    };
  },
  methods: {
    async getProjectData() {
      const url = baseURI + 'projects/' + this.$route.params.projectId;
      const data = await $http.get(url);
      return data.data;
    },
    async saveProjectData() {

    },
  },
  async created() {
    const data = await this.getProjectData();
    for (let key in data)
      this[key] = data[key];
    if (data.owner = getUsername())
      this.userIsOwner = true;
  },
  async mounted() {

  },
  computed: {}
}
</script>

<style scoped>
.main-container {
  min-height: 100vh;
  margin: 65px 120px;
}

.project-data-container {
  height: 1259px;
  width: 1680px;
  background: #C3C3C3;
  border-radius: 50px;
  padding: 45px 40px;
}

.first-block {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 125px;
}

.data-container {
  display: flex;
  flex-direction: column;
  width: 936px;
  height: 351px;
}

.cover-container {
  width: 624px;
  height: 351px;
}

.cancel-button {
  width: 238px;
}

.save-button {
  width: 238px;
}
</style>