<template>
  <Header></Header>
  <div class="catalog-container">
    <profiles-list
        class="user-cards-container"
        :profiles-list="userCards"
    >
    </profiles-list>
  </div>
  <div ref="observer" class="observer"></div>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import $http, {baseURI} from "@/api";
import ProfilesList from "@/modules/ProfilesList/components/ProfilesList.vue";

export default {
  name: "CatalogPage",
  components: {ProfilesList, Footer, Header},
  data() {
    return {
      page: 0,
      count: 12,
      userCards: [],
    };
  },
  created() {
    this.getUserCards();
  },
  mounted() {
    const options = {
      rootMargin: "0px",
      threshold: 1.0,
    };

    const callback = async (entries, observer) => {
      if (entries[0].isIntersecting) {
        await this.getUserCards();
      }
    };

    const observer = new IntersectionObserver(callback, options);
    observer.observe(this.$refs.observer);
  },
  methods: {
    async getUserCards() {
      const url = baseURI + 'get_profile_cards';
      const params = {
        page: this.page,
        count: this.count,
      };
      this.page++;
      const cards = (await $http.get(url, {params: params})).data;
      this.userCards = [...this.userCards, ...cards];
    }
  }
}
</script>

<style scoped>
.catalog-container {
  width: 100%;
  display: flex;
  justify-content: center;
}
.user-cards-container {
  margin-top: 70px;
  width: 1680px;
}
.observer {
  height: 50px;
  background: #111111;
  opacity: 0;
}
input {
  border-radius: 80px;
}
</style>