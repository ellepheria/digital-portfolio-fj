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
            profile_picture: '',
            cover_path: '',
            profile_picture_path: '',
            dragOver: false,
        }
    },
    methods: {
        async saveNewProfileData() {
            const data = this.getThisProfileData();
            await this.$store.dispatch('profile/editData', data).then(res => alert('Данные сохранены успешно'));
        },
        async uploadProfileCover() {
            const formData = new FormData();
            formData.append('cover', this.cover);
            let response = {};
            await $http.post(baseURI + 'upload_profile_cover', formData)
                .then(res => {
                    response = res;
                    this.cover_path = baseURI + res.data.cover_path
                });
            return response;
        },
        async uploadProfilePicture() {
            const formData = new FormData();
            formData.append('profile_picture', this.profile_picture);
            let response = {};
            await $http.post(baseURI + 'upload_profile_picture', formData)
                .then(res => {
                    response = res;
                    this.profile_picture_path = baseURI + res.data.profile_picture_path;
                });
            return response;
        },
        getCurrentProfileData() {
            const data = this.$store.getters['profile/getCurrentData'];
            this.updateProfileData(data);
        },
        updateProfileData(data) {
            for (let key in data) {
                this[key] = data[key];
            }
        },
        getThisProfileData() {
            const vuexData = this.$store.getters['profile/getCurrentData'];
            const data = {};
            for (let key in vuexData) {
                if (key != 'cover_path' && key != 'profile_picture_path')
                    data[key] = this[key];
            }
            return data;
        },
        dragLeaveHandler(event) {
            event.preventDefault();
            this.dragOver = false;
        },
        dragOverHandler(event) {
            event.preventDefault();
            this.dragOver = true;
        },
        async coverUpload(event) {
            event.preventDefault();
            this.cover = event.target.files[0];
            await this.uploadProfileCover();
        },
        async dragCoverUpload(event) {
            event.preventDefault();
            this.cover = event.dataTransfer.files[0];
            await this.uploadProfileCover();
        },
        async profilePictureUpload(event) {
            event.preventDefault();
            this.profile_picture = event.target.files[0];
            await this.uploadProfilePicture();
        },
        async dragProfilePictureUpload(event) {
            event.preventDefault();
            this.profile_picture = event.dataTransfer.files[0];
            await this.uploadProfilePicture();
        },
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
    beforeCreate() {
        if (!this.$store.getters['auth/isAuthenticated']) {
            this.$router.push('/auth');
        }
    },
    async created() {
        await this.$store.dispatch('profile/getCurrentProfileData').then(res => {
            const data = res;
            data.cover = ($http.get(data.cover_path)).data;
            data.profile_picture = ($http.get(data.profile_picture_path)).data;
            this.updateProfileData(data);
        });

    }
}