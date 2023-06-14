<template>
  <Header></Header>
  <div class="form-container">
    <form @submit.prevent="saveProjectData" class="form">
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
              v-model="short_description"
              type="text"
              class="short-description">
        </div>
        <div class="cover-container">
          <img v-if="coverUploaded" :src="getImagePath(this.cover_path)" alt="" class="cover">
          <img v-if="!coverUploaded" src="@/assets/img.png" alt="" class="cover">
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

        </div>
        <div class="links-container">
          <input type="text" class="added_links">
        </div>
      </div>
      <div class="forth-block">
        <div class="add-photo-button">
          <BlueButton class="add-photo-button">
            Добавить фотографии проекта
          </BlueButton>
        </div>
        <div class="buttons">
          <RedButton class="cancel-button">
            Отменить
          </RedButton>
          <BlueButton
              class="save-button"
              type="submit">
            Сохранить
          </BlueButton>
        </div>
      </div>
    </form>
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

export default {
  name: "ProjectEditPage",
  components: {BlueButton, RedButton, Footer, Header},
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
      const data = {}

      data.title = this.title;
      data.short_description = this.short_description;
      data.description = this.description;
      data.added_links = this.added_links;
      data.owner = getUsername();

      const uri = baseURI + `projects/${this.$route.params.projectId}/edit`;
      await $http.post(uri, data)
          .then(res => alert('данные сохранены успешно'))
          .catch(res => alert('Что-то пошло не так'))
    },
    getImagePath(imagePath) {
      return baseURI + imagePath;
    }
  },
  async created() {
    const data = await this.getProjectData();
    for (let key in data)
      this[key] = data[key];
    console.log(data.owner)
    console.log(getUsername())
    if (data.owner == getUsername())
      this.userIsOwner = true;
  },
  async mounted() {

  },
  computed: {
    coverUploaded() {
      return !!this.cover_path;
    }
  }
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
  margin-top: 40px;
  margin-bottom: 40px;
  border-radius: 40px;
}
.cover {
  width: 624px;
  height: 351px;
  border-radius: 40px;
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

.add-photo-button {
  width: 433px;
}

.save-button {
  width: 238px;
  margin-left: 45px;
}

.cancel-button {
  width: 238px;
}
</style>