<template>
  <div class="container">
    <Header></Header>
    <div class="form-container">
      <form class="form">
        <div class="form-title">Добавление проекта</div>
        <div class="data-container">
          <div class="title-label label">
            Название проекта
          </div>
          <input
              v-model="title"
              class="title"
              type="text">
          <div class="short-description-label label">
            Краткое описание
          </div>
          <input
              v-model="short_description"
              type="text"
              class="short-description">
          <div class="description-label label">
            Описание проекта
          </div>
          <input
              v-model="description"
              type="text"
              class="description">
        </div>
        <div class="buttons">
          <BlueButton
              class="save-button"
              @clicked="addProject"
              type="submit">
            Добавить проект
          </BlueButton>
        </div>
      </form>
    </div>
    <Footer></Footer>
  </div>

</template>

<script>
import $http, {baseURI} from "@/api";
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import RedButton from "@/UI/Buttons/RedButton/RedButton.vue";
import BlueButton from "@/UI/Buttons/BlueButton/BlueButton.vue";
import {getUsername} from "@/helpers";


export default {
  name: "ProjectEditPage",
  components: {
    BlueButton,
    RedButton,
    Footer,
    Header,
  },
  data() {
    return {
      title: '',
      short_description: '',
      description: '',
    };
  },
  methods: {
    async addProject() {
      let response;
      const url = baseURI + 'create_project';
      const payload = {
        title: this.title,
        short_description: this.short_description,
        description: this.description,
      }
      await $http.post(url, payload)
          .then(res => this.$router.push('/' + getUsername() + '/portfolio'));
    },
  },
  created() {
    this.title = 'Project';
  },
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  justify-content: space-between;
}
input {
  text-align: center;
  border: none;
}
.label {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 300;
  font-size: 20px;
  line-height: 160%;
  color: #EAEAEA;
}
.form-title {
  width: 100%;
  text-align: center;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 50px;
  line-height: 160%;
  color: #FFFFFF;
}
.form-container {
  width: 1680px;
  background: #C3C3C3;
  border-radius: 50px;
  margin: 45px auto;
  padding-top: 45px;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.data-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 346px;
  width: 95%;
  margin: 0 40px;
}
.title {
  border-radius: 20px;
  height: 90px;
  width: 100%;
}
.short-description-label {
  margin-top: 20px;
}
.short-description {
  border-radius: 40px;
  height: 251px;
  width: 100%;
}
.description-label {
  margin-top: 20px;
}
.description {
  border-radius: 40px;
  height: 150px;
  width: 100%;
}
.buttons {
  display: flex;
  justify-content: flex-end;
  margin: 40px 45px;
}
.save-button {
  width: 238px;
  margin-left: 45px;
}
</style>