<template>
  <button class="blue-button" :type="type" @click.prevent="$emit('clicked')">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "BlueButton",
  emits: ['clicked'],
  props: {
    type: 'button',
  }
}
</script>

<style scoped>
.blue-button {
  height: 50px;
  background: #CFFCFF;
  border-radius: 55px;
  border: 1px solid #61E5E9;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 26px;
  line-height: 120%;
  color: #2CCDD1;
}

.blue-button:hover {
  cursor: pointer;
  background: #c0f3f6;
}
</style>