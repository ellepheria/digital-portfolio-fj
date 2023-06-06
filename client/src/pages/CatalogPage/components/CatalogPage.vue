<template>
  <Header></Header>
  <div class="user-cards-container">
    <profiles-list
        :profiles-list="userCards"
    >
    </profiles-list>
    <div ref="observer" class="observer"></div>
  </div>
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
  mounted() {
    const options = {
      rootMargin: "0px",
      threshold: 1.0,
    };

    const callback = (entries, observer) => {
      if (entries[0].isIntersecting) {
        this.getUserCards();
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
      for (let i = 0; i < cards.length; i++) {
        cards[i]['images'].cover_path = baseURI + cards[i]['images'].cover_path;
        cards[i]['images'].profile_picture_path = baseURI + cards[i]['images'].profile_picture_path;
      }
      this.userCards = [...this.userCards, ...cards];
    }
  }
}
</script>

<style scoped>
.user-cards-container{
  margin: 40px;
}
.observer {
  height: 30px;
  background: none;
}
</style>