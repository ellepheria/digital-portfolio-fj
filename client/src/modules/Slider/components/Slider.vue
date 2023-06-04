<template>
  <div class="slider-container">
    <slider-helper v-bind="options">
      <div class="item">1</div>
      <div class="item">2</div>
      <div class="item">3</div>
      <div class="item">4</div>
      <div class="item">5</div>
      <div class="item">6</div>
      <div class="item">7</div>
      <div class="item">8</div>
      <div class="item">9</div>
      <div class="item">10</div>
      <div class="item">11</div>
      <div class="item">12</div>
      <div class="item">13</div>
      <div class="item">14</div>
    </slider-helper>
  </div>
</template>

<script>
import SliderHelper from "@/modules/Slider/components/slider-helper.vue";

export default {
  name: "Slider",
  components: {SliderHelper},
  data() {
    return {
      options: {
        items: 1,
        margin: 40,
        nav: true,
        dots: true,
        loop: true,
        offset: 1,
        prevNav: 'Назад',
        nextNav: 'Далее',
        sibling: true,
      },
    };
  },
}
</script>

<style scoped>
.slider-container {
  margin: 40px;
}

.attach {
  width: 100%;
  max-width: 1000px;
  min-width: 480px;
  padding: 50px 15px;
  margin: 0 auto;
  position: relative;
}

.slider_case {
  margin-bottom: 40px;
}

.item {
  background: #00800b;
  text-align: center;
  padding: 100px 0;
  color: #fff;
  font-size: 26px;
  font-style: italic;
  font-weight: 300;
}

.item.active {
  background: #ff3f4d;
}

.item.super {
  background: #04a0c5;
}

pre {
  border:1px solid #eee;
  padding:15px;
  background: #f5f5f5;
}
</style>