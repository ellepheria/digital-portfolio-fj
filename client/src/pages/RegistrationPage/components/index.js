import * as ui from "@/UI";
import RegistrationForm from "@/modules/RegistrationForm";
import {getUsername} from "@/helpers";

export default {
    name: "RegistrationPage",
    components: {RegistrationForm, ...ui},
    beforeCreate() {
        if (this.$store.getters['auth/isAuthenticated']) {
            this.$router.push(`${getUsername()}`)
        }
    },
}