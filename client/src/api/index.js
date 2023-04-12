import axios from "axios";

const baseURI = 'http://192.168.0.5:8080/'

export {
    baseURI
};

const $http = axios.create({
    baseURI,
});

export default $http;