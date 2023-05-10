<template>
  <Header></Header>
  <div class="container">
    <div class="card-container">
      <div class="card-preview">
        <div class="cover-container">
          <img
              v-if="coverUploaded"
              :src="cover_path"
              class="cover"
          >
        </div>
        <div class="profile-picture-container">
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
    </div>
    <div class="data-container">
      <div class="data-field-container">
        <div class="name label">
          Имя:
        </div>
        <div class="name field">
          {{ name }}
        </div>
      </div>
      <div class="data-field-container">
        <div class="username label">
          Username:
        </div>
        <div class="username field">
          {{ username }}
        </div>
      </div>
      <div class="data-field-container">
        <div class="type_of_activity label">
          Род деятельности:
        </div>
        <div class="type_of_activity field">
          {{ type_of_activity }}
        </div>
      </div>
      <div class="data-field-container" v-if="surname">
        <div class="surname label">
          Фамилия:
        </div>
        <div class="surname field">
          {{ surname }}
        </div>
      </div>
      <div class="data-field-container" v-if="age">
        <div class="age label">
          Возраст:
        </div>
        <div class="age field">
          {{ age }}
        </div>
      </div>
      <div class="data-field-container" v-if="phone_number">
        <div class="phone_number label">
          Телефон:
        </div>
        <div class="phone_number field">
          {{ phone_number }}
        </div>
      </div>
      <div class="data-field-container" v-if="about">
        <div class="about label">
          О себе:
        </div>
        <div class="about field-area">
          {{ about }}
        </div>
      </div>
      <div class="data-field-container" v-if="education">
        <div class="education label">
          Образование:
        </div>
        <div class="education field">
          {{ education }}
        </div>
      </div>
      <div class="data-field-container" v-if="technologies">
        <div class="technologies label">
          Используемые технологии:
        </div>
        <div class="technologies field">
          {{ technologies }}
        </div>
      </div>
      <div class="data-field-container" v-if="social_networks">
        <div class="social_networks label">
          Социальные сети:
        </div>
        <div class="social_networks field">
          {{ social_networks }}
        </div>
      </div>
    </div>
  </div>
  <div class="portfolio-container">
    <projects-list>
      <div class="list-title"></div>
    </projects-list>
  </div>
  <Footer></Footer>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>