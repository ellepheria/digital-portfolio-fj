import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import $http, {baseURI} from "@/api";
import {AxiosHeaders} from "axios";
import ProjectsList from "@/modules/ProjectsList/components/ProjectsList.vue";

export default {
    name: "ProfilePage",
    components: {ProjectsList, Footer, Header},
    data() {
        return {
            name: '',
            surname: '',
            username: '',
            age: '',
            type_of_activity: '',
            phone_number: '',
            about: '',
            education: '',
            technologies: '',
            social_networks: '',
            cover_path: '',
            profile_picture_path: '',
        }
    },
    methods: {
        async getProfileData() {
            const data = (await $http.get(
                baseURI + 'get_profile/' + this.$route.params.username,
            )).data;

            for (let key in data) {
                this.$data[key] = data[key];
            }
            this.profile_picture_path = baseURI + this.profile_picture_path;
            this.cover_path = baseURI + this.cover_path;
        },
    },
    async created() {
        await this.getProfileData();
    },
    computed: {
        coverUploaded() {
            return !!this.cover_path;
        },
        profilePictureUploaded() {
            return !!this.profile_picture_path;
        },
        isAuth() {
            return this.$store.getters['auth/isAuthenticated'];
        }
    }
}