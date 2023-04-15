<template>
  <div class="nav-bar">
    <div class="logo">
      Future Job
    </div>
    <button class="registration" @click="this.$router.push('/registration')">
      Регистрация
    </button>
  </div>
  <div class="main">
    <div class="auth-form-container">
      <h1 class="form-title">
        Авторизация
      </h1>
      <div class="form-fields">
        <input
            v-model="username"
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
          <div class="remember_me__label">Запомнить?</div>
        </div>
        <button class="auth-button" @click="authorizationFormSubmit">
          Вход
        </button>
      </div>
      <a href="/forgot-password" class="forgot-password">
        Забыли пароль?
      </a>
    </div>
  </div>
  <div class="footer">
    Работает на OpenSource: <a href="https://github.com/ellepheria/digital-portfolio-fj">GitHub</a>
  </div>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>