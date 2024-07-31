//更改用户状态信息
export const userStatus = (state, user) =>{
    //判断用户是否存在
    if (user!=null){
        state.user_name = JSON.parse(user).user_name;
        state.user_id = JSON.parse(user).user_id;
        state.is_login = true;
    }else if (user==null){
        //登出时清空sessionStroage里面的参数
        sessionStorage.setItem("user",null);
        sessionStorage.setItem("userToken",'');
        state.currentUser = null;
        state.is_login = false;
        state.assign='';
    }
}
//更改token
export const setToken = (state,token) =>{
    if (token!=null){
        state.token = token;
    }else {
        state.token = '';
    }
}