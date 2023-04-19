<template>
<div class="form-container">
  <form @submit.prevent @submit="saveNewProfileData">
    <input
        type="text"
        v-model="name"
        placeholder="Имя*">
    <input
        type="text"
        v-model="surname"
        placeholder="Фамилия">
    <input
        type="text"
        v-model="username"
        placeholder="Username">
    <input
        type="text"
        v-model="age"
        placeholder="Возраст">
    <input
        type="text"
        v-model="phone"
        placeholder="Телефон">
    <input
        type="text"
        v-model="about"
        placeholder="О себе">
    <input
        type="text"
        v-model="type_of_activity"
        placeholder="Род деятельности">
    <input
        type="text"
        v-model="education"
        placeholder="Образование">
    <input
        type="text"
        v-model="technologies"
        placeholder="Технологии">
    <input
        type="text"
        v-model="social_networks"
        placeholder="Социальные сети">
    <button type="submit">Сохранить</button>
  </form>
  <button @click="getCurrentProfileData">Отменить</button>
</div>
</template>

<script src="./index.js"></script>

<style scoped src="./style.css"></style>