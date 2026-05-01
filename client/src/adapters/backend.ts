import axios from "axios";
import { showNotification } from "../helpers/notification";

const BASE_URL = import.meta.env.VITE_API_BASE_URL as string;

const pendingTimers = new WeakMap<any, any>();

axios.interceptors.request.use((config) => {
    if (config.url?.startsWith(BASE_URL)) {
        const timer = setTimeout(() => {
            showNotification("Starting Backend, might take upto 60secs.");
        }, 5000);
        pendingTimers.set(config, timer);
    }
    return config;
});

axios.interceptors.response.use(
    (response) => {
        const timer = pendingTimers.get(response.config);
        if (timer) {
            clearTimeout(timer);
            pendingTimers.delete(response.config);
        }
        return response;
    },
    (error) => {
        if (error.config) {
            const timer = pendingTimers.get(error.config);
            if (timer) {
                clearTimeout(timer);
                pendingTimers.delete(error.config);
            }
        }
        return Promise.reject(error);
    }
);

export const fetchUserData = async () => {
    try {
        const { data } = await axios.get(BASE_URL + "/auth/me", {
            withCredentials: true
        });
        return data;
    } catch (error: any) {
        if (error.response && error.response.data) {
            throw error.response.data;
        }
        throw { message: "Network error or server is unreachable", code: "NETWORK_ERROR" };
    }
}

export const login = async ({ email, password }: { email: string; password: string }) => {
    try {
        await axios.post(BASE_URL + "/auth/login", { email, password }, {
            withCredentials: true
        });
    } catch (error: any) {
        if (error.response && error.response.data) {
            throw error.response.data;
        }
        throw { message: "Network error or server is unreachable", code: "NETWORK_ERROR" };
    }
}

export const register = async ({ email, password, firstName, lastName }: { email: string; password: string; firstName: string; lastName: string }) => {
    try {
        await axios.post(BASE_URL + "/auth/register", { email, password, first_name: firstName, last_name: lastName }, {
            withCredentials: true
        });
    } catch (error: any) {
        if (error.response && error.response.data) {
            throw error.response.data;
        }
        throw { message: "Network error or server is unreachable", code: "NETWORK_ERROR" };
    }
}

export const logout = async () => {
    try {
        await axios.get(BASE_URL + "/auth/logout", {
            withCredentials: true
        });
    } catch (error: any) {
        if (error.response && error.response.data) {
            throw error.response.data;
        }
        throw { message: "Network error or server is unreachable", code: "NETWORK_ERROR" };
    }
}
