import * as ui from "@/UI"
import $http from "@/api";
import {baseURI} from "@/api";

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
            type_of_activity: '',
            cover: '',
            profilePhoto: '',
            dragOver: false,
        }
    },
    methods: {
        async saveNewProfileData() {
            const data = this.getThisProfileData();
            this.$store.dispatch('profile/editData', data);
            await this.uploadProfileFiles().then(res => console.log(res));
        },
        async uploadProfileFiles() {
            const formData = new FormData();
            formData.append('cover', this.cover);
            formData.append('profile_picture', this.profilePhoto)
            await $http.post(baseURI + 'upload_profile_files', formData);
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
        },
        getThisProfileData() {
            const vuexData = this.$store.getters['profile/getCurrentData'];
            const data = {};
            for (let key in vuexData) {
                data[key] = this[key];
            }
            console.log(data)
            return data;
        },
        getCoverSrc() {
            return URL.createObjectURL(this.cover);
        },
        getProfilePhotoSrc() {
            return URL.createObjectURL(this.profilePhoto);
        },
        dragLeaveHandler(event) {
            event.preventDefault();
            this.dragOver = false;
        },
        dragOverHandler(event) {
            event.preventDefault();
            this.dragOver = true;
        },
        coverUpload(event) {
            event.preventDefault();
            console.log(event);
            this.cover = event.target.files[0];
        },
        dragCoverUpload(event) {
            event.preventDefault();
            this.cover = event.dataTransfer.files[0];
        },
        profilePictureUpload(event) {
            event.preventDefault();
            console.log(event);
            this.profilePhoto = event.target.files[0];
        },
        dragProfilePictureUpload(event) {
            event.preventDefault();
            this.profilePhoto = event.dataTransfer.files[0];
        },
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
    },
    beforeCreate() {
        if (!this.$store.getters['auth/isAuthenticated']) {
            this.$router.push('/auth');
        }
    },
    async created() {
        const data = await this.$store.dispatch('profile/getCurrentProfileData');
        this.updateProfileData(data);
    }
}