<template>
  <Header></Header>
  <div class="container">
    <div class="card-container">
      <div class="card-preview">
        <div class="cover-container">
          <img
              v-if="coverUploaded"
              :src="getCoverSrc()"
              class="cover"
          >
        </div>
        <div class="profile-picture-container">
          <img
              v-if="profilePictureUploaded"
              :src="getProfilePictureSrc()"
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

    </div>
  </div>
  <Footer></Footer>
</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>