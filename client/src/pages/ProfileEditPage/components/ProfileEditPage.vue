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
          <blue-button
              class="change-password-button">Смена пароля</blue-button>
        </div>
        <div class="save-cancel-block">
          <red-button
              class="cancel-button"
              @clicked="getCurrentProfileData">Отмена</red-button>
          <blue-button
            class="save-button"
            @clicked="saveNewProfileData">Сохранить</blue-button>
        </div>
      </div>
      <div class="form-container">
        <form @submit.prevent @submit="saveNewProfileData">
          <div class="data-field-container">
            <div class="name label">
              Имя:
            </div>
            <input class="name field" v-model="name" />
          </div>
          <div class="data-field-container">
            <div class="username label">
              Username:
            </div>
            <input class="username field" v-model="username" />
          </div>
          <div class="data-field-container">
            <div class="type_of_activity label">
              Род деятельности:
            </div>
            <input class="type_of_activity field" v-model="type_of_activity" />
          </div>
          <div class="data-field-container">
            <div class="surname label">
              Фамилия:
            </div>
            <input class="surname field" v-model="surname" />
          </div>
          <div class="data-field-container">
            <div class="age label">
              Возраст:
            </div>
            <input class="age field" v-model="age" />
          </div>
          <div class="data-field-container">
            <div class="phone_number label">
              Телефон:
            </div>
            <input class="phone_number field" v-model="phone_number" />
          </div>
          <div class="data-field-container">
            <div class="about label">
              О себе:
            </div>
            <textarea class="about field" v-model="about" />
          </div>
          <div class="data-field-container">
            <div class="education label">
              Образование:
            </div>
            <input class="education field" v-model="education" />
          </div>
          <div class="data-field-container">
            <div class="technologies label">
              Используемые технологии:
            </div>
            <input class="technologies field" v-model="technologies" />
          </div>
          <div class="data-field-container">
            <div class="social_networks label">
              Социальные сети:
            </div>
            <input class="social_networks field" v-model="social_networks" />
          </div>
        </form>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>