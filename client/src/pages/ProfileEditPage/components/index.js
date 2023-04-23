import * as ui from "@/UI"

export default {
    name: "ProfileEditPage",
    components: {...ui},
    data() {
        return {
            name: '',
            surname: '',
            username: '',
            age: '',
            phone_number: '',
            about: '',
            education: '',
            technologies: '',
            social_networks: '',
            type_career: '',
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
            for (let key in data) {
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
    },
    mounted() {
        const data = this.$store.getters['profile/getCurrentData'];
        this.updateProfileData(data);
    }
}