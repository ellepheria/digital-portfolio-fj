<template>
  <Header></Header>
  <div class="search-container">
    <input
        v-model="searchValue"
        placeholder="Поиск..."
        type="text"
        class="search">
    <button
        @click="searchUserCards"
        class="search-btn">Найти</button>
  </div>
  <div class="catalog-container">
    <profiles-list
        v-if="!!this.userCards"
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
      searchValue: '',
      searchPage: 0,
      searched: false,
    };
  },
  created() {
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
  watch: {
    searchValue(newValue, oldValue) {
      if (!!oldValue && !newValue && this.searched) {
        this.searched = false;
        this.page = 0;
        this.getUserCards();
      }
    },
  },
  methods: {
    searchUserCards() {
      this.searched = true;
      this.searchPage = 0;
      this.getUserCards();
    },
    async getUserCards() {
      if (!this.searchValue) {
        const url = baseURI + 'get_profile_cards';
        const params = {
          page: this.page,
          count: this.count,
        };
        const cards = (await $http.get(url, {params: params})).data;
        if (!cards.error) {
          this.userCards = [...this.userCards, ...cards];
          this.page++;
        }
      }
      else {
        const uri = baseURI + 'search_users';
        const params = {
          page: this.searchPage,
          count: this.count,
          search_query: this.searchValue,
        };
        if (this.searchPage == 0) {
          const cards = (await $http.get(uri, {params: params})).data;
          if (!cards.error) {
            this.userCards = cards;
            this.searchPage++;
          }
        }
        else {
          const cards = (await $http.get(uri, {params: params})).data;
          if (!cards.error) {
            this.userCards = [...this.userCards, ...cards];
            this.searchPage++;
          }
        }
      }
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}
.search-container {
  width: 100%;
  margin-top: 70px;
  flex-direction: row;
  display: flex;
  justify-content: center;
}
.search {
  width: 1425px;
  height: 50px;
  border-top-left-radius: 80px;
  border-bottom-left-radius: 80px;
  background: #F9F9F9;
  border: 1px solid #D3D3D3;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0 32px;
}
.search-btn {
  width: 200px;
  height: 50px;
  border-top-right-radius: 80px;
  border-bottom-right-radius: 80px;
  background: #2CCDD1;
  border: 1px solid #2CCDD1;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 26px;
  line-height: 120%;
  color: #FFFFFF;
  cursor: pointer;
}
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
</style>