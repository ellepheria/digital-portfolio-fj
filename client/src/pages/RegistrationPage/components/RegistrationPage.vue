<template>
  <div class="container">
    <Header></Header>
    <div class="main">
      <PageLogo></PageLogo>
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
    <Footer></Footer>
  </div>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>