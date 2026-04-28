import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_BASE_URL as string;

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
