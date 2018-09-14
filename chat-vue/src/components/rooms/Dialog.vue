<template>
    <mu-col span="8" xl="9">
        <mu-container class="dialog">
            <mu-row v-for="dialog in dialogs"
                    direction="column"
                    justify-content="start"
                    align-items="end">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </mu-row>
        </mu-container>
        <mu-container>
            <mu-row>
                <mu-text-field v-model="form.textarea"
                               multi-line :rows="4" f
                               ull-width
                               placeholder="Введите текст сообщения">
                </mu-text-field>
                <mu-button class="btn-send" round color="success">Отправить</mu-button>
            </mu-row>
        </mu-container>
    </mu-col>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Dialog",
        props: {
            id: '',
        },
        data() {
            return {
                dialogs: '',
                form: {
                    textarea: '',
                }
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadDialog()
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
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
