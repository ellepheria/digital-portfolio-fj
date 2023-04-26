import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";

export default {
    name: "ProfilePage",
    components: {Footer, Header},
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
            cover: '',
            profilePicture: '',
        }
    },
    methods: {
        async getProfileData() {
            const data = await this.$store.dispatch(
                'profile/getCurrentProfileData',
                this.$route.params.username
            );

            for (let key in data) {
                this.$data[key] = data[key];
            }
        },
        async getProfileImages() {
            // get profile images cover and profilePic
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