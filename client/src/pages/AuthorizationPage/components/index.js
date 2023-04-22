export default {
    name: "AuthorizationPage",
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
            } else {
              this.$store.dispatch('profile/getCurrentProfileData', data.username);
            }

            return this.$router.push({ path: `/${data.username}/edit` });
        },
    },
}