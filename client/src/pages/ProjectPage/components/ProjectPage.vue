<template>
  <Header></Header>
  <div class="header">{{title}}</div>
  <div class="main-container">

    <slider class="slider"></slider>

    <div class="project-data-container">
      <div class="description">
        {{description}}
      </div>
    </div>

  </div>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import $http, {baseURI} from "@/api";
import Slider from "@/modules/Slider/components/Slider.vue";

export default {
  name: "ProjectPage",
  components: {Slider, Footer, Header},
  data() {
    return {
      title: '',
      short_description: '',
      description: '',
      added_links: {},
      cover_path: '',
      images: {},
      owner: '',
    };
  },
  methods: {
    async getProjectData() {
      const uri = baseURI + 'projects/' + this.$route.params.projectId;
      const {data} = await $http.get(uri);
      for (let key in data) {
        this[key] = data[key];
      }
    }
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

.slider {
  margin-bottom: 100px;
}

.project-data-container {
  padding: 40px;
  display: flex;
  flex-direction: column;
  width: 100%;
  background: #C3C3C3;
  border-radius: 50px;
}

.description {
  background: #FFFFFF;
  width: 100%;
  border-radius: 40px;
  min-height: 200px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 120%;
  display: flex;
  align-items: center;
  text-align: center;
}
</style>