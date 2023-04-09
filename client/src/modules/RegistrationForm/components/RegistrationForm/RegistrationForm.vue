<template>
  <div>
    <form id="form" class="registration_form" @submit.prevent>
      <input
          v-model="login"
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
          placeholder="Password">
      <input
          type="checkbox"
          class="checkbox"
          v-model="check"
          checked
      >
      <button
          class="confirm_button"
          @click="registrationFormSubmit"
      >click me</button>
    </form>
  </div>
</template>

<script>
import ConfirmButton from "@/UI/ConfirmButton/ConfirmButton.vue";

export default {
  name: "RegistrationForm",
  components: {
    ConfirmButton,
  },
  data() {
    return {
      login: '',
      username: '',
      password: '',
      check: true
    }
  },
  methods: {
    registrationFormSubmit(e) {
      console.log(e)
    },
  }
}
</script>

<style scoped>
.registration_form {
  max-width: 70%;
  display: flex;
  flex-direction: column;
  margin: auto;

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