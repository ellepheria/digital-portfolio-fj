import * as ui from "@/UI";

export default {
    name: "RegistrationPage",
    components: {...ui},
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

            this.$store.dispatch('profile/clearProfileState');
            this.$store.dispatch('profile/setLocalData', {username: this.username})
            return this.$router.push({ path: `/${username}/edit` });
        },
    },
}