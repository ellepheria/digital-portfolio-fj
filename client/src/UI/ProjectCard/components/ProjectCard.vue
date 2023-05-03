<template>
  <div class="project-card">
    <div class="meta-container">
      <div class="number">{{ this.$props.number.padStart(2, 0) }}</div>
      <div class="container">
        <div class="title">{{ this.$props.title }}</div>
        <div class="description">{{ this.$props.shortDescription }}</div>
      </div>
    </div>
    <div class="arrow-container">
      <div class="arrow">
        <div></div>
      </div>
    </div>
    <div class="cover-container">
      <img v-if="!!this.$props.cover" :src="this.$props.cover" class="cover-image">
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectCard",
  props: {
    title: '',
    shortDescription: '',
    cover: '',
    number: 0,
  }
}
</script>

<style scoped>
.project-card {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  height: 310px;
  background: #c4c4c4;
  border-radius: 50px;
  margin: 40px 0;
  padding-left: 50px;
  padding-right: 20px;
}

.meta-container {
  display: flex;
  flex-direction: row;
  justify-content: left;
}

.number {
  font-family: 'Playfair Display';
  font-style: normal;
  font-weight: 700;
  font-size: 100px;
  line-height: 160%;
  font-feature-settings: 'pnum' on, 'lnum' on;
  color: #FFFFFF;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 50px;
}

.title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 26px;
  line-height: 160%;
  text-align: left;
  color: #FFFFFF;
  max-width: 450px;
}

.description {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 120%;
  text-align: left;
  color: #FFFFFF;
  max-width: 450px;
}

.arrow-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.arrow {
  position: relative;
  width: 300px;
  height: 50px;
  margin: 20px;
}

.arrow div {
  position: relative;
  top: 20px;
  width: 300px;
  height: 10px;
  background-color: #fff;
  box-shadow: 0 3px 5px rgba(0, 0, 0, .2);
  left: 0;
  display: block;
}

.arrow div::after {
  content: '';
  position: absolute;
  width: 40px;
  height: 10px;
  top: -11px;
  right: -8px;
  background-color: #FFFFFF;
  transform: rotate(45deg);
}

.arrow div::before {
  content: '';
  position: absolute;
  width: 40px;
  height: 10px;
  top: 11px;
  right: -8px;
  background-color: #FFFFFF;
  box-shadow: 0 3px 5px rgba(0, 0, 0, .2);
  transform: rotate(-45deg);
}

.arrow:hover {
  animation: arrow-1 1s linear infinite;
}

@keyframes arrow {
  0% {
    left: 0;
  }
  50% {
    left: 10px;
  }
  100% {
    left: 0;
  }
}

.cover-container {
  height: 270px;
  max-width: 480px;
  width: 100%;
  border-radius: 40px;
  background: #fff;
  margin: 20px 0;
}
</style>