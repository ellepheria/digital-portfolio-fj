<template>
  <div class="container">
    <Header></Header>
    <div class="main">
      <div class="preview-container">
        <div class="card-preview">
          <img src="@/assets/ground.jpg" height="200" width="502">
          <span class="name-data">{{name}}</span>
          <span class="type_of_activity-data">{{type_of_activity}}</span>
          <span class="about-data">{{about}}</span>
        </div>
        <div class="buttons">
          <div class="change-password-block">
            <button class="change-password-button button">Смена пароля</button>
          </div>
          <div class="save-cancel-block">
            <button class="save-button button" type="submit">Сохранить</button>
            <button class="cancel-button button" @click="getCurrentProfileData">Отменить</button>
          </div>
        </div>
      </div>
      <div class="form-container">
        <form @submit.prevent @submit="saveNewProfileData">
          <div class="first-container">
            <div class="block">
              <input
                  type="text"
                  class="form-field first-block"
                  v-model="name"
                  placeholder="Имя*"
                  required>
              <input
                  type="text"
                  class="form-field first-block"
                  v-model="username"
                  placeholder="Username"
                  required>
              <input
                  type="text"
                  class="form-field first-block"
                  v-model="type_of_activity"
                  placeholder="Род деятельности">
            </div>
            <div class="block">
              <input
                  type="text"
                  class="form-field first-block"
                  v-model="surname"
                  placeholder="Фамилия">
              <input
                  type="text"
                  class="form-field first-block"
                  v-model="age"
                  placeholder="Возраст">
              <input
                  type="tel"
                  class="form-field first-block"
                  v-model="phone_number"
                  placeholder="Телефон">
            </div>
          </div>
          <div class="second-container">
        <textarea
            class="about form-field"
            type="textarea"
            v-model="about"
            placeholder="О себе">
        </textarea>
          </div>
          <div class="third-container">
            <input
                type="text"
                class="form-field second-block"
                v-model="education"
                placeholder="Образование">
            <input
                type="text"
                class="form-field second-block"
                v-model="technologies"
                placeholder="Технологии">
            <input
                type="text"
                class="form-field second-block"
                v-model="social_networks"
                placeholder="Социальные сети">
          </div>
        </form>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script src="./index.js"></script>

<style scoped src="./style.css"></style>