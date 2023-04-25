import * as ui from "@/UI";
import AuthForm from "@/modules/AuthForm";
import {getUsername} from "@/helpers";

export default {
    name: "AuthorizationPage",
    components: {AuthForm, ...ui},
    beforeCreate() {
        if (this.$store.getters['auth/isAuthenticated']) {
            this.$router.push(`${getUsername()}`)
        }
    },
}