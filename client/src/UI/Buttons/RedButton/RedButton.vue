<template>
  <button class="red-button" @click="$emit('clicked')">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "RedButton",
  emits: ['clicked'],
}
</script>

<style scoped>
.red-button {
  height: 50px;
  background: #FFD4D4;
  border-radius: 55px;
  border: 1px solid #EF4343;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 26px;
  line-height: 120%;
  color: #FF0000;
}

.red-button:hover {
  cursor: pointer;
  background: #f6c5c5;
}
</style>