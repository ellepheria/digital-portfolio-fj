import Header from "@/UI/Header/components/Header.vue";
import Footer from "@/UI/Footer/components/Footer.vue";
import ProfileCard from "@/UI/ProfileCard";
import $http, {baseURI} from "@/api";
import ProjectsList from "@/modules/ProjectsList/components/ProjectsList.vue";

export default {
    name: "ProfilePage",
    components: {ProjectsList, Footer, Header, ProfileCard},
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
            projectsList: [],
            page: 0,
            count: 6,
        }
    },
    methods: {
        async getProjects() {
            const username = this.$route.params.username;
            const params = {
                count: this.count,
                page: this.page,
            };
            this.page++;
            const uri = baseURI + 'get_user_projects/' + username;
            let projectsList = (await $http.get(uri, {params : params}))
                .data.json_list;
            this.projectsList = [...this.projectsList, ...projectsList];
        },
        async getProfileData() {
            const data = (await $http.get(
                baseURI + 'get_profile/' + this.$route.params.username,
            )).data;

            for (let key in data) {
                this.$data[key] = data[key];
            }
            this.profile_picture_path = this.profile_picture_path ? baseURI + this.profile_picture_path : '';
            this.cover_path = this.cover_path ? baseURI + this.cover_path : '';
        },
    },
    async created() {
        await this.getProfileData();
        await this.getProjects();
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
    },
    mounted() {
        const options = {
            rootMargin: "0px",
            threshold: 1.0,
        };

        const callback = (entries, observer) => {
            if (entries[0].isIntersecting) {
                this.getProjects();
            }
        };

        const observer = new IntersectionObserver(callback, options);
        observer.observe(this.$refs.observer);
    }
}