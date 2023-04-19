export default {
    name: "RegistrationPage",
    data() {
        return {
            email: '',
            username: '',
            password: '',
            confirmPassword: '',
            check: true
        }
    },
    methods: {
        async registrationFormSubmit() {
            const email = this.email;
            const username = this.username;
            const password = this.password;

            const { data } = await this.$store.dispatch('auth/register', {
                email,
                username,
                password,
            });

            if (!data) {
                return; //тут надо обрабатывать ошибки
            }

            return this.$router.push({ path: `/${username}/edit` });
        },
        logout() {
            this.$store.dispatch('auth/logout')
        }
    },
}