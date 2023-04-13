<template>
  <div>
    <form id="form" class="registration_form" @submit.prevent>
      <input
          v-model="login"
          class="input login"
          type="text"
          placeholder="Email/Username">
      <input
          @input="password = $event.target.value"
          v-model="password"
          class="input password"
          type="password"
          placeholder="Пароль">
      <input
          type="checkbox"
          class="checkbox"
          v-model="rememberMe"
          id="remember_me"
          checked
      >
      <label for="remember_me">Запомнить?</label>
      <button
          class="confirm_button"
          @click="authorizationFormSubmit"
      >click me</button>
    </form>
  </div>
</template>

<script>
import ConfirmButton from "@/UI/ConfirmButton/ConfirmButton.vue";



export default {
  name: "AuthorizationPage",
  components: {
    ConfirmButton,
  },
  data() {
    return {
      login: '',
      password: '',
      rememberMe: true
    }
  },
  methods: {
    async authorizationFormSubmit() {
      const { login, password, rememberMe} = this;
      console.log(login);
      console.log(password);
      console.log(rememberMe);
      const { data } = await this.$store.dispatch('auth/login', {
        login,
        password,
        rememberMe,
      });

      if (!data) {
        return; //тут надо обрабатывать ошибки
      }

      return this.$router.push({ path: '/' });
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
  margin-top: 15px;
  padding: 10px 15px;
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