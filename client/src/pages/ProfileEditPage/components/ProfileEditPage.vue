<template>
  <div class="container">
    <Header></Header>
    <div class="main">
      <div class="preview-container">
        <div class="card-preview">
          <div class="cover-container">
            <input
                type="file"
                accept="image"
                class="cover-input"
                draggable="true"
                @dragleave="dragLeaveHandler"
                @dragover="dragOverHandler"
                @drop="dragCoverUpload"
                @change="coverUpload">
            <span v-if="!dragOver && !coverUploaded">Вставьте изображение для обложки</span>
            <span v-if="dragOver && !coverUploaded">Отпустите фото, чтобы загрузить</span>
            <img
                v-if="coverUploaded"
                :src="cover_path"
                class="cover"
            >
          </div>
          <div class="profile-picture-container">
            <input
                type="file"
                accept="image"
                class="profile-picture-input"
                draggable="true"
                @drop="dragProfilePictureUpload"
                @change="profilePictureUpload">
            <img
                v-if="profilePictureUploaded"
                :src="profile_picture_path"
                class="profile-picture">
            <img
                v-if="!profilePictureUploaded"
                src="@/assets/defaultProfilePicture.png"
                class="profile-picture">
          </div>
          <div class="text-fields">
            <p class="name-data text-field">{{ username }}</p>
            <p class="type_of_activity-data text-field">{{ type_of_activity }}</p>
          </div>
          <p class="about-data text-field">{{ about }}</p>
        </div>
        <div class="change-password-block">
          <button class="change-password-button button">Смена пароля</button>
        </div>
        <div class="save-cancel-block">
          <button class="save-button button" @click="saveNewProfileData">Сохранить</button>
          <button class="cancel-button button" @click="getCurrentProfileData">Отмена</button>
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
                  placeholder="Род деятельности"
                  required>
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