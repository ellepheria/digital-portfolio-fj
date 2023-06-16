<template>
  <Header></Header>
  <div class="form-container">
    <form class="form">
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
          <input
              type="file"
              accept="image"
              class="cover-input"
              draggable="true"
              @dragleave="dragLeaveHandler"
              @dragover="dragOverHandler"
              @drop="dragCoverUpload"
              @change="coverUpload">
          <span v-if="!dragOver && !coverUploaded">Вставьте изображение для обложки</span>
          <span v-if="dragOver && !coverUploaded">Отпустите фото, чтобы загрузить</span>
          <img
              v-if="coverUploaded"
              :src="getImagePath(this.cover_path)"
              class="cover"
          >
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
          <BlueButton
              @clicked="this.$refs['upload-photo'].click()"
              class="add-photo-button">
            Добавить фотографии проекта
          </BlueButton>
        </div>
        <div class="buttons">
          <RedButton class="cancel-button">
            Отменить
          </RedButton>
          <BlueButton
              class="save-button"
              @clicked.prevent="saveProjectData"
              type="submit">
            Сохранить
          </BlueButton>
        </div>
      </div>
    </form>
  </div>
  <input
      @change.prevent="uploadImages"
      multiple
      ref="upload-photo"
      type="file"
      class="upload-photo">
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
      addedImages: {},
      dragOver: false,
      cover: '',
    };
  },
  methods: {
    async uploadCover(e) {
      const formData = new FormData();
      formData.append('cover', this.cover);
      const uri = baseURI + '/' + this.$route.params.projectId + '/upload_cover'
      let response = {};
      await $http.post(uri, formData)
          .then(res => {
            response = res;
            this.cover_path = res.data.cover_path
          });
      return response;
    },
    async uploadImages(e) {
      const fileList = e.target.files;
      const formData = new FormData();
      for (let index = 0; index < fileList.length; index++) {
        formData.append(`${index}`, fileList[index])
      }
      const uri = baseURI + this.$route.params.projectId + '/upload_photos'
      await $http.post(uri, formData)
          .then(res => console.log(res));
    },
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
    },
    dragLeaveHandler(event) {
      event.preventDefault();
      this.dragOver = false;
    },
    dragOverHandler(event) {
      event.preventDefault();
      this.dragOver = true;
    },
    async coverUpload(event) {
      event.preventDefault();
      this.cover = event.target.files[0];
      await this.uploadCover();
    },
    async dragCoverUpload(event) {
      event.preventDefault();
      this.cover = event.dataTransfer.files[0];
      await this.uploadCover();
    },
  },
  async created() {
    const data = await this.getProjectData();
    for (let key in data)
      this[key] = data[key];
    if (data.owner == getUsername())
      this.userIsOwner = true;
  },
  computed: {
    coverUploaded() {
      return !!this.cover_path;
    },
    imagesUploaded() {
      return !!this.images;
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
  position: relative;
}
.cover {
  width: 624px;
  height: 351px;
  border-radius: 40px;
}
.cover-input {
  opacity: 0;
  height: 100%;
  width: 100%;
  position: absolute;
}
span {
  width: 100%;
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