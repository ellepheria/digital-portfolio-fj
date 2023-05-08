import {createApp, h} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {BlueButton, RedButton} from '@/UI/Buttons/index' ;

const app = createApp(App)

app.component('RedButton', RedButton);
app.component('BlueButton', BlueButton);

app.use(store);
app.use(router);
app.mount('#app');
