<template>
  <Header></Header>
  <div class="projects-container">
    <div class="projects-not-added" v-if="projectsList.length < 1">
      Проекты еще не добавлены
    </div>
    <projects-list
        v-if="projectsList.length > 0"
        :projects-list="projectsList"
    ></projects-list>
  </div>
  <div ref="observer" class="observer"></div>
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
      const username = this.$route.params.username;
      const params = {
        count: this.count,
        page: this.page,
      };
      this.page++;
      const uri = baseURI + 'get_user_projects/' + username;
      let projectsList = (await $http.get(uri, {params : params}))
          .data.json_list;
      this.projectsList = [...this.projectsList, ...projectsList.sort((a, b) => a.id - b.id)];
    },
  },
  mounted() {
    const options = {
      rootMargin: "0px",
      threshold: 1.0,
    };

    const callback = (entries, observer) => {
      if (entries[0].isIntersecting) {
        this.getProjects();
      }
    };

    const observer = new IntersectionObserver(callback, options);
    observer.observe(this.$refs.observer);
  }
}
</script>

<style scoped>
.projects-container {
  margin-left: 40px;
  margin-right: 40px;
}

.observer {
  height: 30px;
  background: none;
}
</style>