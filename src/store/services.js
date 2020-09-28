import axios from "axios"
const newConnectoraabbcde = axios.create({
  baseURL:
    "https://crowdbotics-slack-dev.herokuapp.com/dashboard/app/11907/storyboard/11240/",
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
const plugin11 = axios.create({
  baseURL:
    "https://crowdbotics-slack-dev.herokuapp.com/dashboard/app/7307/storyboard/8491/",
  headers: { Accept: "application/json", "Content-Type": "application/json" }
})
export const apiService = {}
