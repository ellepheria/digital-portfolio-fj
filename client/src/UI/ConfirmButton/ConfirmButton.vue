<template>
  <button >
    {{textButton}}
  </button>
</template>

<script>
export default {
  name: "ConfirmButton",
  data: {
    textButton: ''
  },
  props: {
    textButton: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>

</style>