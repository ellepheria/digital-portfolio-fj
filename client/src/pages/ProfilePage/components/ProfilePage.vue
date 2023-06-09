<template>
  <Header></Header>

  <div class="container">
    <profile-card
        :name="name"
        :type_of_activity="type_of_activity"
        :about="about"
        :profile_picture_path="profile_picture_path"
        :cover_path="cover_path"
    ></profile-card>
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
    <div class="list-title">Портфолио пользователя</div>
    <projects-list
        :projects-list="projectsList"
    >
    </projects-list>
    <div ref="observer" class="observer"></div>
  </div>
  <Footer></Footer>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>