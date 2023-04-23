<template>
  <Header></Header>
  <div class="form-container">
    <form @submit.prevent @submit="saveNewProfileData">
      <div class="first-container">
        <div class="block">
          <input
              type="text"
              v-model="name"
              placeholder="Имя*"
              required>

          <input
              type="text"
              v-model="username"
              placeholder="Username"
              required>
          <input
            type="text"
            v-model="type_career"
            placeholder="Род деятельности">
        </div>
        <div class="block">
          <input
              type="text"
              v-model="surname"
              placeholder="Фамилия">
          <input
              type="text"
              v-model="age"
              placeholder="Возраст">
          <input
              type="tel"
              v-model="phone_number"
              placeholder="Телефон">
        </div>
      </div>
      <div class="second-container">
      <textarea
          class="about"
          type="textarea"
          v-model="about"
          placeholder="О себе">
      </textarea>
      </div>
      <div class="third-container">
        <input
            type="text"
            v-model="education"
            placeholder="Образование">
        <input
            type="text"
            v-model="technologies"
            placeholder="Технологии">
        <input
            type="text"
            v-model="social_networks"
            placeholder="Социальные сети">
      </div>
      <button type="submit">Сохранить</button>
    </form>
    <button @click="getCurrentProfileData">Отменить</button>
  </div>
  <Footer></Footer>
</template>

<script src="./index.js"></script>

<style scoped src="./style.css"></style>