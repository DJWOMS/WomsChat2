<template>
    <mu-col span="4" xl="2" class="rooms-list">
        <mu-button @click="addRoom">Создать комнату</mu-button>
        <div v-for="room in rooms">
            <h3 @click="openDialog(room.id)">{{room.creater.username}}</h3>
            <small>{{room.date}}</small>
        </div>
    </mu-col>
</template>

<script>
    export default {
        name: "Room",
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRoom()
        },
        methods: {
            // Загружаю список комнат
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            },
            openDialog(id) {
                this.$emit("openDialog", id)
            },
            // Создание комнаты
            addRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "POST",
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    h3 {
        cursor: pointer;
    }
    .rooms-list {
        margin: 0 10px 0 0;
        box-shadow: 1px 4px 5px #848181;
    }
</style>
