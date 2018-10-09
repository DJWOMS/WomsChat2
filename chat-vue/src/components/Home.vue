<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            Чат на vue js
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
            <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
        </mu-appbar>
        <mu-row>
            <h1></h1>
        </mu-row>
        <!--<mu-row>-->
            <!--<Room v-if="auth" @openDialog="openDialog"></Room>-->
            <!--<Dialog v-if="dialog.show" :id="dialog.id"></Dialog>-->
            <!--<slot></slot>-->
        <!--</mu-row>-->
        <slot></slot>
    </mu-container>
</template>

<script>
    // import Room from '@/components/rooms/Room.vue'
    // import Dialog from '@/components/rooms/Dialog.vue'

    export default {
        name: "Home",
        // components: {
        //     Room,
        //     Dialog
        // },
        data() {
            return {
                dialog: {
                    id: '',
                    show: false,
                }
            }
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            // Открываю диалог
            // openDialog(id) {
                // this.dialog.id = id
                // this.dialog.show = true
            // }
        },
    }
</script>

<style scoped>

</style>
