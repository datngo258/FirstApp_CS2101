import axios from "axios";

const HOST = "https://thanhduong.pythonanywhere.com/";

export const endpoints = {
  categories: "/categories/",
  courses : "/courses"
};


export const authAPI = axios.create({
  baseURL: HOST,
  headers: { 
    Authorization: `Bearer ...` 
  }
});

// API cơ bản
export default axios.create({
  baseURL: HOST
});
