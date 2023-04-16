<template>
  <div class="container">
    <div class="nav-bar">
      <div class="logo">
        Future Job
      </div>
      <button class="auth-button" @click="this.$router.push('/auth')">
        Вход
      </button>
    </div>
    <div class="main">
      <div class="page-logo-container">
        Future Job
      </div>
      <div class="registration-form">
        <h1 class="form-title">
          Регистрация
        </h1>
        <div class="form-fields">
          <input
              v-model="email"
              type="email"
              placeholder="Email"
              class="form-fields__field">
          <input
              v-model="username"
              type="text"
              placeholder="Username"
              class="form-fields__field">
          <input
              v-model="password"
              type="password"
              placeholder="Введите пароль"
              class="form-fields__field">
          <input
              v-model="confirmPassword"
              type="password"
              placeholder="Подтвердите пароль"
              class="form-fields__field">
        </div>
        <div class="form-buttons">
          <button class="registration-button" @click="registrationFormSubmit">
            Далее
          </button>
        </div>
      </div>
    </div>
    <div class="footer">
      Работает на OpenSource: <a href="https://github.com/ellepheria/digital-portfolio-fj">GitHub</a>
    </div>
  </div>

</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>