<template>
    <div>
        <input v-model="login" type="text" placeholder="Логин"/>
        <input v-model="password" type="password" placeholder="Пароль"/>
        <button @click="setLogin">Войти</button>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://104.248.174.91/auth/token/create/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Спасибо что Вы с нами")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Логин или пароль не верен")
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
