<template>
  <div class="nav-bar">
      <div class="logo" @click="this.$router.push('/catalog')">
        Future Job
      </div>
    <div class="buttons not_auth" v-if="!isAuth">
      <blue-button
          @clicked="this.$router.push('/auth')"
          class="auth-button btn">
        Вход
      </blue-button>
      <blue-button
          @clicked="this.$router.push('/registration')"
          class="registration-button btn">
        Регистрация
      </blue-button>
    </div>
    <div class="buttons auth" v-if="isAuth">
      <blue-button
          v-if="layout == 'default' || layout == 'ProfileEdit'"
          @clicked="this.$router.push('/' + getUsername() + '/portfolio')"
          class="portfolio btn">
        Портфолио
      </blue-button>
      <red-button
          v-if="layout == 'ProfileEdit'"
          @clicked="logout"
          class="logout-button btn"
      >Выход
      </red-button>
      <blue-button
          v-if="!ownProfile"
          class="profile"
          @clicked="this.$router.push('/' + getUsername())">
        Профиль
      </blue-button>
      <blue-button
          v-if="layout == 'default' && ownProfile"
          class="profile_edit btn"
          @clicked="this.$router.push(getUsername() + '/edit')">
        Редактировать
      </blue-button>
      <blue-button
          v-if="layout == 'Portfolio'"
          @clicked="this.$router.push('/add_project')"
          class="add-project btn">Добавить проект
      </blue-button>
      <BlueButton
          v-if="projectEdit"
          @clicked="onProjectEdit"
          class="project-edit-button"
      >
        Редактировать
      </BlueButton>
    </div>
  </div>
</template>

<script>
import BlueButton from "@/UI/Buttons/BlueButton/BlueButton.vue";
import {getUsername} from "@/helpers";
import $http, {baseURI} from "@/api";

export default {
  name: "Header",
  components: {BlueButton},
  props: {
    projectEdit: false,
  },
  methods: {
    getUsername,
    logout() {
      this.$store.dispatch('auth/logout');
      this.$store.dispatch('profile/clearProfileState');
      this.$router.push('/auth');
    },
    addProject() {
      this.$router.push('/add_project');
    },
    onProjectEdit() {
      this.$router.push(this.$route.params.projectId + '/edit')
    },
  },
  computed: {
    isAuth() {
      return this.$store.getters['auth/isAuthenticated'];
    },
    layout() {
      return this.$route.meta.layout;
    },
    ownProfile() {
      return this.$route.params.username == getUsername();
    }
  }
}
</script>

<style scoped>
.nav-bar {
  min-height: 110px;
  width: 100%;
  border-bottom: 3px solid #D9D9D9;
  display: flex;
  justify-content: space-between;
  background: #FFFFFF;
}
a {
  text-decoration: none;
}
.btn {
  margin-top: 30px;
  margin-right: 50px;
}
.portfolio {
  width: 170px;
}
.profile {
  width: 170px;
  margin-right: 50px;
}
.profile_edit {
  width: 210px;
}
.auth-button {
  width: 100px;
}
.registration-button {
  width: 190px;
}
.logout-button {
  width: 120px;
}
.add-project {
  width: 250px;
}
.logo {
  margin: 14px 46px;
  height: 58px;
  width: 253px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 50px;
  line-height: 160%;
  color: #6ACED0;
  cursor: pointer;
}
.project-edit-button {
  width: 230px;
  margin-right: 50px;
}
</style>