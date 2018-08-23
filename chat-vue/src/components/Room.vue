<template>
    <div>
        <ul>
            <li v-for="room in rooms">
                <h3>{{room.creater.username}}</h3>
                {{room.date}}
            </li>
        </ul>
    </div>
</template>

<script>
    import $ from 'jquery'

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
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
