<template>
  <div class="registration-form">
    <form>
      <h1 class="form-title">
        Регистрация
      </h1>
      <div class="form-fields">
        <input
            v-model="email"
            type="email"
            placeholder="Email"
            required
            class="form-fields__field">
        <input
            v-model="username"
            type="text"
            placeholder="Username"
            required
            class="form-fields__field">
        <input
            v-model="password"
            type="password"
            placeholder="Введите пароль"
            required
            class="form-fields__field">
        <input
            v-model="confirmPassword"
            type="password"
            placeholder="Подтвердите пароль"
            required
            class="form-fields__field">
      </div>
      <div class="form-buttons">
        <blue-button class="registration-button" @clicked="registrationFormSubmit">
          Далее
        </blue-button>
      </div>
    </form>
  </div>
</template>

<script>
import * as ui from "@/UI";
import { setUsername } from "@/helpers";
import BlueButton from "@/UI/Buttons/BlueButton/BlueButton.vue";

export default {
  name: "RegistrationForm",
  components: {...ui},
  data() {
    return {
      email: '',
      username: '',
      password: '',
      confirmPassword: '',
    }
  },
  methods: {
    async registrationFormSubmit() {
      const email = this.email;
      const username = this.username;
      const password = this.password;

      if (this.password !== this.confirmPassword) {
        alert('Пароли должны совпадать');
        return;
      }

      const { data } = await this.$store.dispatch('auth/register', {
        email,
        username,
        password,
      });

      if (data.error) {
        alert(data.error);
        return;
      }

      setUsername(this.username);
      return this.$router.push({ path: `/${username}/edit` });
    },
  },
}
</script>

<style scoped>
.registration-form {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  background: #C3C3C3;
  border-radius: 80px;
  width: 594px;
  height: 620px;
  padding: 0 134px;
  margin: 0 auto;
}

.form-title {
  color: #000;
  font-weight: 400;
  font-size: 50px;
  line-height: 160%;
  margin-bottom: 35px;
  margin-top: 40px;
}

.form-fields__field {
  font-weight: 500;
  font-size: 18px;
  width: 100%;
  height: 50px;
  border: #fff;
  border-radius: 80px;
  margin-bottom: 40px;
  text-align: center;
}

.form-buttons {
  display: flex;
  justify-content: center;
}

.registration-button {
  width: 100%;
}
</style>