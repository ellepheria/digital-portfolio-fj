<template>
  <div>
    <form id="form" class="registration_form" @submit.prevent="registrationFormSubmit">
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
      <button
      type="submit">
        Submit
      </button>
    </form>
  </div>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>