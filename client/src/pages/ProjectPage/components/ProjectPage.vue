<template>
  <Header></Header>
  <div class="main-container">
    {{title}}
    {{short_description}}
    {{description}}
    {{cover_path}}
    {{images}}
    {{owner}}
  </div>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import $http, {baseURI} from "@/api";

export default {
  name: "ProjectPage",
  components: {Footer, Header},
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

</style>