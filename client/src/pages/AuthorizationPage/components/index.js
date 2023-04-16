import ConfirmButton from "@/UI/ConfirmButton/ConfirmButton.vue";
export default {
    name: "AuthorizationPage",
    components: {
        ConfirmButton,
    },
    data() {
        return {
            login: '',
            password: '',
            rememberMe: true
        }
    },
    methods: {
        async authorizationFormSubmit() {
            const { login, password, rememberMe} = this;
            const { data } = await this.$store.dispatch('auth/login', {
                login,
                password,
                rememberMe,
            });

            if (!data) {
                return; //тут надо обрабатывать ошибки
            }

            return this.$router.push({ path: '/' });
        },
    },
}