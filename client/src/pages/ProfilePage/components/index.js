export default {
    name: "ProfilePage",
    data() {
        return {
            name: '',
            surname: '',
            username: 'test',
            age: '',
            type_of_activity: '',
            phone: '',
            about: '',
            education: '',
            technologies: '',
            social_networks: '',
        }
    },
    methods: {
        async getData() {
            const {data} = await this.$store.dispatch('profile/getCurrentProfileData', this.username);
            for (let key in data) {
                this.$data[key] = data[key];
            }
        }
    }
}