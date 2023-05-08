<template>
  <div class="nav-bar">
    <div class="logo">
      Future Job
    </div>
    <div class="buttons not_auth" v-if="!this.$store.getters['auth/isAuthenticated']">
      <blue-button
          @clicked="this.$router.push('/auth')"
          class="auth-button btn">
        Вход
      </blue-button>
      <blue-button
          class="registration-button btn"
          @clicked="this.$router.push('/registration')"
      >
        Регистрация
      </blue-button>
    </div>
    <div class="buttons auth" v-if="this.$store.getters['auth/isAuthenticated']">
      <red-button
          @clicked="logout"
          class="logout-button btn"
      >Выйти</red-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
      this.$store.dispatch('profile/clearProfileState');
      this.$router.push('/auth');
    },
  },
}
</script>

<style scoped>
.nav-bar {
  height: 110px;
  width: 100%;
  border-bottom: 3px solid #D9D9D9;
  display: flex;
  justify-content: space-between;
  background: #FFFFFF;
}

.btn {
  width: 190px;
  margin-top: 20px;
  margin-right: 50px;
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
}
</style>