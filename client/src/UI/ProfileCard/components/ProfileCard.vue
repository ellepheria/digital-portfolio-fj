<template>
  <div class="card-block">
    <router-link :to="'/' + username">
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
            <p class="name-data text-field">{{ name }}</p>
            <p class="type_of_activity-data text-field">{{ type_of_activity }}</p>
          </div>
          <p class="about-data text-field">{{ about }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ProfileCard",
  props: {
    name: '',
    about: '',
    type_of_activity: '',
    profile_picture_path: '',
    cover_path: '',
    username: '',
  },
  computed: {
    profilePictureUploaded(){
      return !!this.$props.profile_picture_path;
    },
    coverUploaded() {
      return !!this.$props.cover_path
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
}
.card-block {
  display: flex;
  justify-content: center;
}
.card-container {
  display: flex;
  flex-direction: column;
  height: 650px;
  width: 502px;
}

.card-preview {
  display: flex;
  flex-direction: column;
  background: #C3C3C3;
  height: 548px;
  border-radius: 40px;
  position: relative;
}

.cover-container {
  background: #eee;
  height: 200px;
  width: 100%;
  border-radius: 40px 40px 0 0;
  position: relative;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.cover {
  height: 100%;
  width: 100%;
  border-radius: 40px 40px 0 0;
  object-fit: cover;
}

.profile-picture-container {
  border-radius: 50%;
  height: 130px;
  width: 130px;
  justify-content: center;
  position: absolute;
  left: 185.5px;
  top: 142.5px;

}

.profile-picture {
  height: 100%;
  width: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.text-fields {
  margin-top: 82px;
  display: flex;
  flex-direction: column;
}

.text-field {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 160%;
  text-align: center;
  color: #FFFFFF;
}
</style>