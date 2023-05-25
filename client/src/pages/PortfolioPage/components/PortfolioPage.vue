<template>
  <Header></Header>
  <projects-list
      :projects-list="projectsList"
  ></projects-list>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import ProjectsList from "@/modules/ProjectsList/components/ProjectsList.vue";
import $http, {baseURI} from "@/api";
import {getUsername} from "@/helpers";

export default {
  name: "PortfolioPage",
  components: {ProjectsList, Footer, Header},
  data() {
    return {
      projectsList: [],
      count: 6,
      page: 0,
    }
  },
  methods: {
    async getProjects() {
      const username = getUsername();
      const params = {
        count: this.count,
        page: this.page,
      };
      const uri = baseURI + 'get_user_projects/' + username;
      await $http.get(uri, {params : params})
          .then(res => console.log(res.data));
    },
  },
  async created() {
    this.projectsList = await this.getProjects();
  }
}
</script>

<style scoped>

</style>