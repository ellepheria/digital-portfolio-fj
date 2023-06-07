<template xmlns:BlueButton="http://www.w3.org/1999/xlink">
  <Header></Header>
  <div class="form-container">
    <form @submit.prevent="addProject" class="form">
      <div class="first-block">
        <div class="data-container">
          <div class="title-label">
            Название проекта
          </div>
          <input
              v-model="title"
              class="title"
              type="text">
          <div class="short-description-label">
            Краткое описание
          </div>
          <input
              v-model="shortDescription"
              type="text"
              class="short-description">
        </div>
        <div class="cover-container">
          a
        </div>
      </div>
      <div class="second-block">
        <input
            v-model="description"
            type="text"
            class="description">
      </div>
      <div class="third-block">
        <div class="slider-container">
          <slider></slider>
        </div>
        <div class="links-container">
          <input type="text" class="added_links">
        </div>
      </div>
      <div class="forth-block">
        <div class="add-photo-button">
          <BlueButton>
            Добавить фотографии проекта
          </BlueButton>
        </div>
        <div class="buttons">
          <RedButton>Назад</RedButton>
          <BlueButton
              type="submit">Добавить
          </BlueButton>
        </div>
      </div>
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
import Slider from "@/modules/Slider/components/Slider.vue";

export default {
  name: "AddProjectPage",
  components: {Slider, BlueButton, RedButton, Footer, Header},
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
.form-container {
  width: 1680px;
  height: 1259px;
  background: #C3C3C3;
  border-radius: 50px;
  margin: 45px auto;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.first-block {
  display: flex;
  flex-direction: row;
  width: 936px;
  justify-content: space-between;
}

.data-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 346px;
  width: 936px;
  margin: 45px 40px;
}

.cover-container {
  width: 624px;
  height: 351px;
  margin: 40px 40px 45px;
}

.title {
  border-radius: 20px;
  height: 50px;
  width: 936px;
}

.short-description {
  border-radius: 40px;
  height: 251px;
  width: 936px;
}

.second-block {
  margin: 0 40px;
}

.description {
  border-radius: 40px;
  height: 150px;
  width: 100%;
}

.third-block {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.forth-block {
  margin: 45px 40px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>