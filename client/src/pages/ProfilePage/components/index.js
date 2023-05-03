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
            cover: '',
            profilePicture: '',
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
        },
        async getProfileImages() {
            const data = await $http.get(
                baseURI + 'get_profile_files/' + this.$route.params.username,
            );
            if (data) {
                this.cover = data.data.cover;
                this.profilePicture = data.data.profilePicture;
            };
        },
        getProfilePictureSrc() {
            return URL.createObjectURL(this.profilePicture);
        },
        getCoverSrc() {
            return URL.createObjectURL(this.cover);
        },
    },
    async created() {
        await this.getProfileData();
        await this.getProfileImages();
    },
    computed: {
        coverUploaded() {
            return !!this.cover;
        },
        profilePictureUploaded() {
            return !!this.profilePhoto;
        },
        isAuth() {
            return this.$store.getters['auth/isAuthenticated'];
        }
    }
}