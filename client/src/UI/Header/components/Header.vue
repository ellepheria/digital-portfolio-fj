<template>
  <div class="nav-bar">
    <div class="logo">
      Future Job
    </div>
    <div class="buttons not_auth" v-if="!this.$store.getters['auth/isAuthenticated']">
      <button class="auth-button" @click="this.$router.push('/auth')">
        Вход
      </button>
      <button class="registration-button" @click="this.$router.push('/registration')">
        Регистрация
      </button>
    </div>
    <div class="buttons auth" v-if="this.$store.getters['auth/isAuthenticated']">
      <button class="auth-button" @click="logout">
        Выйти
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  methods: {
    logout() {
      this.$store.dispatch('auth/logout');
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
}

.auth-button {
  text-align: center;
  width: 190px;
  height: 50px;
  border-radius: 80px;
  border: none;
  background: #2ccdd1;
  font-weight: 400;
  font-size: 22px;
  line-height: 160%;
  margin-top: 20px;
  margin-right: 62px;
}

.auth-button:hover {
  cursor: pointer;
  background: #208875;
}

.registration-button {
  text-align: center;
  width: 190px;
  height: 50px;
  border-radius: 80px;
  border: none;
  background: #2ccdd1;
  font-weight: 400;
  font-size: 22px;
  line-height: 160%;
  margin-top: 20px;
  margin-right: 62px;
}

.registration-button:hover {
  cursor: pointer;
  background: #208875;
}

.logo {
  margin: 14px 46px;
  height: 58px;
  width: 253px;
  font-size: 50px;
  line-height: 160%;
  color: #6ACED0;
}
</style>