<template>
  <div class="auth-form">
    <h1 class="form-title">
      Авторизация
    </h1>
    <div class="form-fields">
      <input
          v-model="login"
          type="text"
          placeholder="Email/Username"
          class="form-fields__field">
      <input
          v-model="password"
          type="password"
          placeholder="Введите пароль"
          class="form-fields__field">
    </div>
    <div class="form-buttons">
      <div class="remember-me-container">
        <input
            v-model="rememberMe"
            type="checkbox"
            class="remember_me"
            checked>
        <div
            class="remember_me__label"
            @click="rememberMe=!rememberMe"
        >Запомнить?
        </div>
      </div>
      <button class="auth-button" @click="authorizationFormSubmit">
        Вход
      </button>
    </div>
    <a href="/forgot-password" class="forgot-password">
      Забыли пароль?
    </a>
  </div>
</template>

<script>
import * as ui from "@/UI";
import { setUsername } from "@/helpers";

export default {
  name: "AuthForm",
  components: {...ui},
  data() {
    return {
      login: '',
      password: '',
      rememberMe: true
    }
  },
  methods: {
    async authorizationFormSubmit() {
      const { login, password, rememberMe } = this;
      const { data } = await this.$store.dispatch('auth/login', {
        login,
        password,
        rememberMe,
      });

      if (!data) {
        return; //тут надо обрабатывать ошибки
      } else {
        setUsername(data.username);
      }

      return this.$router.push({ path: `/${data.username}/edit` });
    },
  },
}

</script>

<style scoped>
.auth-form {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  background: #C3C3C3;
  border-radius: 80px;
  width: 594px;
  height: 620px;
  padding: 80px 134px 61px;
  margin: 0 auto;
}

.form-title {
  color: #000;
  font-weight: 400;
  font-size: 50px;
  line-height: 160%;
  margin-bottom: 68px;
}

.form-fields__field {
  font-weight: 500;
  font-size: 18px;
  width: 100%;
  height: 50px;
  border: #fff;
  border-radius: 80px;
  margin-bottom: 56px;
  text-align: center;
}

.form-buttons {
  display: flex;
  justify-content: space-between;
  margin-bottom: 50px;
}

.auth-button {
  text-align: center;
  width: 153px;
  height: 50px;
  border-radius: 80px;
  border: none;
  background: #2ccdd1;
  font-weight: 400;
  font-size: 22px;
  line-height: 160%;
}

.auth-button:hover {
  cursor: pointer;
  background: #208875;
}

.remember-me-container {
  display: flex;
  padding-top: 15px;
}

.remember_me {
  background: #FFFFFF;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  margin-right: 14px;
  margin-top: 1px;
}

.remember_me__label {
  font-size: 14px;
  font-weight: 400;
  width: 97px;
  height: 21px;
  cursor: pointer;
}

.forgot-password {
  margin: 0 90px;
}
</style>