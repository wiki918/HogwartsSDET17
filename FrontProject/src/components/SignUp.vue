<template>
  <div class="sign-up">
    <h1>注册</h1>
    <v-text-field label="用户名" v-model="username" outlined clearable></v-text-field>
    <v-text-field label="密码" type="password" v-model="password" outlined clearable></v-text-field>
    <v-text-field label="邮箱" v-model="email" outlined clearable></v-text-field>
    <v-btn color="primary" @click="register()">注册</v-btn>
    <v-btn color="primary" text @click="signIn()">已有账号，去登录</v-btn>
  </div>
</template>

<script>
  export default {
    name: "SignUp",
    data(){
      return{
        username:'',
        password:'',
        email:''
      }
    },
    methods:{
      signIn(){
        this.$router.push({name:'SignIn'})
      },
      register(){
        let post_data = {
          userName: this.username,
          password: this.password,
          email: this.email
        }
        this.$api.user.signUp(post_data).then(res=>{
          console.log(res)
        })
      }
    }
  }
</script>

<style scoped>
  .sign-up{
    width: 500px;
    margin: 0 auto;
    text-align: center;
  }
</style>
