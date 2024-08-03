import axiosInstance from './index'

const axios = axiosInstance
// const ip = 'http://192.168.43.108:8081/app/'
// const ip = 'http://127.0.0.1:8081/app/'
const ip = 'http://127.0.0.1:8000/app/'

export const register = data => {return axios.post(ip+'create_user/', data)}

export const login = data => {return axios.post(ip+'login/', data)}

export const getUserPageScores = data => {return axios.post(ip+'get_user_page_scores/', data)}

export const getUserScoresNumber = data => {return axios.post(ip+'get_user_scores_number/', data)}

export const getASongRandom = data => {return axios.post(ip+'get_a_song_random/', data)}

export const getAClipSongRandom = data => {return axios.post(ip+'clip_get_a_song_random/', data)}

export const updateAMarkedScore = data => {return axios.post(ip+'update_marked_score/', data)}

export const deleteAMarkedScore = data => {return axios.post(ip+'delete_marked_score/', data)}

export const updateAMarkedClip = data => {return axios.post(ip+'update_marked_clip/', data)}

export const deleteAMarkedClip = data => {return axios.post(ip+'delete_marked_clip/', data)}

export const getUserClips = data => {return axios.post(ip+'get_user_clips/', data)}

export const getUserMusicDimensionscore = data => {return axios.post(ip+'get_user_music_dimension_scores/', data)}

export const updateAMarkedDimensionscore = data => {return axios.post(ip+'update_marked_dimension_score/', data)}

export const deleteAMarkedDimensionscore = data => {return axios.post(ip+'delete_marked_dimension_score/', data)}

export const getMarkedScoresByQuery = data => {return axios.post(ip+'get_marked_scores_by_query/', data)}

export const createMarkedScore = data => {return axios.post(ip+'create_marked_score/', data)}

export const createDimensionScore = data => {return axios.post(ip+'create_dimension_score/', data)} ///

export const createMarkedClip = data => {return axios.post(ip+'create_marked_clip/', data)}

export const createMarkedDimensionScore = data => {return axios.post(ip+'create_marked_dimension_score/', data)}

export const getASongID = data => {return axios.post(ip+'get_a_song_id/', data)}

export const updateMusicGenre = data => {return axios.post(ip+'update_music_genre/', data)}

export const updateMusicHarmonyQuantity = data => {return axios.post(ip+'update_music_harmony_quantity/', data)}