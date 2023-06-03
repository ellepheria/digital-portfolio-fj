<template>
  <Header></Header>
  <div class="projects-container">
    <projects-list
        :projects-list="projectsList"
    ></projects-list>
  </div>
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
      return await $http.get(uri, {params : params});
    },
  },
  async created() {
    let projectsList = (await this.getProjects()).data.json_list;
    for (let i = 0; i < projectsList.length; i++) {
      projectsList[i]['cover_path'] = baseURI + projectsList[i]['cover_path'];
    }
    this.projectsList = projectsList;
  }
}
</script>

<style scoped>
.projects-container {
  margin-left: 40px;
  margin-right: 40px;
}
</style>