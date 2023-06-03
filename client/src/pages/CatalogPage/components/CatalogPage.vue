<template>
  <Header></Header>
  <div class="user-cards-container">
    <profiles-list
        :profiles-list="userCards"
    >

    </profiles-list>
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
  async created(){
    const cards = (await this.getUserCards()).data;
    for (let i = 0; i < cards.length; i++) {
      cards[i]['images'].cover_path = baseURI + cards[i]['images'].cover_path;
      cards[i]['images'].profile_picture_path = baseURI + cards[i]['images'].profile_picture_path;
    }
    this.userCards = [...this.userCards, ...cards];
  },
  methods: {
    async getUserCards() {
      const url = baseURI + 'get_profile_cards';
      const params = {
        page: this.page,
        count: this.count,
      };
      this.page++;
      this.count += this.count;
      return await $http.get(url, {params: params});
    }
  }
}
</script>

<style scoped>
.user-cards-container{
  margin: 40px;
}
</style>