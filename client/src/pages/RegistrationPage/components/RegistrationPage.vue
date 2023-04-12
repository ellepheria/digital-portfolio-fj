<template>
  <div>
    <form id="form" class="registration_form" @submit.prevent>
      <input
          v-model="email"
          class="input login"
          type="text"
          placeholder="Email">
      <input
          v-model="username"
          class="input username"
          type="text"
          placeholder="Username">
      <input
          @input="password = $event.target.value"
          v-model="password"
          class="input password"
          type="password"
          placeholder="Пароль">
      <input
          @input="confirmPassword = $event.target.value"
          v-model="confirmPassword"
          class="input password"
          type="password"
          placeholder="Подтвердите пароль">
      <input
          type="checkbox"
          class="checkbox"
          v-model="check"
          id="remember_me"
          checked
      >
      <label for="remember_me">Запомнить?</label>
      <button
          class="confirm_button"
          @click="registrationFormSubmit"
      >click me</button>
    </form>
  </div>
</template>

<script>
import ConfirmButton from "@/UI/ConfirmButton/ConfirmButton.vue";
import axios from "axios";


export default {
  name: "RegistrationPage",
  components: {
    ConfirmButton,
  },
  data() {
    return {
      email: '',
      username: '',
      password: '',
      confirmPassword: '',
      check: true
    }
  },
  methods: {
    async registrationFormSubmit() {
      const email = this.email;
      const username = this.username;
      const password = this.password;

      const { data } = await this.$store.dispatch('auth/register', {
        email,
        username,
        password,
      });

      if (!data) {
        return; //тут надо обрабатывать ошибки
      }

      return this.$router.go({ name: 'catalog' });
    },
  },
}
</script>

<style scoped>
.registration_form {
  max-width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
  height: 100vh;
}

.confirm_button {
  align-self: flex-end;
  margin-top: 10px;
  padding: 10px 10px;
  border: 1px solid;
  border-radius: 15px;
}

.input {
  width: 100%;
  padding: 10px 15px;
  border-radius: 15px;
  margin: 10px;
}

.checkbox {
  align-self: flex-start;
  padding: 10px 15px;
}
</style>