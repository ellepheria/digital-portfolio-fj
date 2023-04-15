import ConfirmButton from "@/UI/ConfirmButton/ConfirmButton.vue";

export default {
    name: "AuthorizationPage",
    components: {
        ConfirmButton,
    },
    data() {
        return {
            username: '',
            password: '',
            rememberMe: true
        }
    },
    methods: {
        async authorizationFormSubmit() {
            const { username, password, rememberMe} = this;
            const { data } = await this.$store.dispatch('auth/login', {
                username,
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