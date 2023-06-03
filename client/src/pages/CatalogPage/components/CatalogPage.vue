<template>
  <Header></Header>
  <div class="user-cards-container">

  </div>
  <Footer></Footer>
</template>

<script>
import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";

export default {
  name: "CatalogPage",
  components: {Footer, Header},
  data() {
    return {
      page: 0,
      count: 12,
      userCards: [],
    };
  },
  async created(){

  },
  methods: {

  }
}
</script>

<style scoped>
.user-cards-container{
  margin: 40px;
}
</style>