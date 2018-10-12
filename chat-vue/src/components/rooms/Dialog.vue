<template>
    <RoomSlot>
        <mu-col span="8" xl="9">
            <AddUsers :room="id"></AddUsers>
            <mu-container class="dialog">
                <mu-row v-for="dialog in dialogs"
                        direction="column"
                        justify-content="start"
                        align-items="end"
                        :key="dialog.id">
                    <p><strong>{{dialog.user.username}}</strong></p>
                    <p>{{dialog.text}}</p>
                    <span>{{dialog.date}}</span>
                </mu-row>
            </mu-container>
            <mu-container>
                <mu-row>
                    <mu-text-field v-model="form.textarea"
                                   multi-line
                                   :rows="4"
                                   full-width
                                   placeholder="Введите текст сообщения">
                    </mu-text-field>
                    <mu-button class="btn-send" round color="success" @click="sendMes">Отправить</mu-button>
                </mu-row>
            </mu-container>
        </mu-col>
    </RoomSlot>
</template>

<script>
    import RoomSlot from './Room'
    import AddUsers from './AddUsers'

    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        components: {
            AddUsers,
            RoomSlot,
        },
        data() {
            return {
                dialogs: '',
                form: {
                    textarea: '',
                },
            }
        },
        mounted() {
            this.loadDialog()
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadDialog()
            setInterval(() => {
                this.loadDialog()
            }, 5000)
        },
        methods: {
            // Загрузка диалога
            loadDialog() {
                $.ajax({
                    url: "http://104.248.174.91/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.$route.params.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            },
            // Отправка сообщения
            sendMes() {
                $.ajax({
                    url: "http://104.248.174.91/api/v1/chat/dialog/",
                    type: "POST",
                    data: {
                        room: this.$route.params.id,
                        text: this.form.textarea
                    },
                    success: (response) => {
                        this.loadDialog()
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
    .dialog {
        border: 1px solid #000;
    }

    .btn-send {
        margin: 60px 0 0 15px;
    }
</style>
