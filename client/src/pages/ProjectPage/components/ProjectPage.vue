<template>
  <Header :project-edit="userIsOwner"></Header>
  <div class="header">{{ title }}</div>
  <div class="main-container">
    <div class="slider-container" v-if="!isEmpty(this.images)">
      <swiper
          :modules="[Pagination]"
          :slides-per-view="1"
          :space-between="50"
          @swiper="onSwiper"
          @slideChange="onSlideChange"
          class="slider"
          :loop="true"
          :grab-cursor="true"
          :pagination="true"
      >
        <swiper-slide
            v-for="image in images"
            class="slide"
        >
          <img :src="getPath(image)" alt="image" class="image">
        </swiper-slide>
      </swiper>
    </div>
    <div class="project-data-container" >
      <div class="description">
        {{ description }}
      </div>
      <div class="links">
        {{ added_links }}
      </div>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import $http, {baseURI} from "@/api";
import {Swiper, SwiperSlide} from 'swiper/vue';
import {Pagination} from "swiper";

import 'swiper/css';
import 'swiper/css/pagination'
import {getUsername} from "@/helpers";

export default {
  name: "ProjectPage",
  components: {
    Footer,
    Header,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      title: '',
      short_description: '',
      description: '',
      added_links: '',
      cover_path: '',
      images: {},
      owner: '',
    };
  },
  computed: {
    userIsOwner() {
      return this.owner == getUsername();
    },
  },
  methods: {
    isEmpty(obj) {
      for (let key in obj)
        return false;
      return true;
    },
    Pagination() {
      return Pagination
    },
    getPath(image_path) {
      return baseURI + image_path;
    },
    onSwiper() {

    },
    onSlideChange() {

    },
    async getProjectData() {
      const uri = baseURI + 'projects/' + this.$route.params.projectId;
      const {data} = await $http.get(uri);
      for (let key in data) {
        this[key] = data[key];
      }
      if (!this.added_links || this.added_links == '{}')
        this.added_links = 'Ссылки не добавлены.';
      if (!this.description)
        this.description = 'Описание не добавлено.';
    },
  },
  async created() {
    await this.getProjectData();
  }
}
</script>

<style scoped>
.main-container {
  margin: 80px 120px 100px;
}
.header {
  margin-top: 60px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 50px;
  line-height: 160%;
  text-align: center;
  color: #5F5F5F;
}
.slider-container {
  padding: 50px 0px;
  margin-bottom: 140px;
  width: 100%;
  height: 1005px;
  background: #C3C3C3;
  border-radius: 50px;
}
.slider {
  margin: 50px auto;
  width: 1440px;
  height: 810px;
  border-radius: 50px;
}
.image {
  width: 1440px;
  height: 810px;
  object-fit: contain;
}
.project-data-container {
  padding: 40px;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 520px;
  justify-content: space-between;
  background: #C3C3C3;
  border-radius: 50px;
}
.description, .links {
  background: #FFFFFF;
  width: 100%;
  border-radius: 40px;
  min-height: 200px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 120%;
  text-align: center;
}
</style>