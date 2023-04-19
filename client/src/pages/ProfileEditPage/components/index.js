export default {
    name: "ProfileEditPage",
    data() {
        return {
            name: '',
            surname: '',
            username: '',
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
        async saveNewProfileData() {
            const data = this.getThisData();
            this.$store.dispatch('profile/editData', data);
        },
        getCurrentProfileData() {
            const data = this.$store.getters['profile/getCurrentData'];
            console.log(data);
            this.updateProfileData(data);
        },
        updateProfileData(data) {
            for (let key in this.$data) {
                this[key] = data[key];
            }
        },
        getThisData() {
            let data = {};
            for (let key in this.$data) {
                data[key] = this[key];
            }
            return data;
        }
    }
}