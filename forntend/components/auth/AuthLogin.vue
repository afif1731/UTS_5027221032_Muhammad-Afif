<template>
    <body>
        <div class="form-div ">
            <nav class="navbar navbar-expand-lg navbar-dark mx-3 mb-16 rounded-3" style="background-color:#2a3843;">
                <div class="container-fluid">
                    <NuxtLink class="navbar-brand h-100 d-inline-block align-baseline" to="/">TAPATAN.LTS</NuxtLink>
                </div>
            </nav>
            <div class="d-flex justify-content-center align-items-center h-75">
                <form class="buat-form border rounded rounded-3">
                    <div>
                        <h2 class="mb-4 text-center">LOGIN</h2>
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label text-center">Email address</label>
                        <input type="email" class="form-control" id="inputEmail" aria-describedby="emailHelp" v-model="email" required />
                    </div>
                    <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label text-center">Password</label>
                        <input type="password" class="form-control" id="inputPassword" v-model="password" required />
                    </div>
                    <div>
                        <p class="my-2 text-center question"> Don't Have an Account? <NuxtLink class="linkin" to="/register">Register Here</NuxtLink></p>
                    </div>
                    <button class="btn btn-primary mt-4" type="button" @click="submitClick()">Submit</button>
                </form>
            </div>
        </div>
    </body>
</template>

<script lang="ts">
import { GameAuth } from '~/assets/game_func/game.client';

export default {
    data() {
        return {
            email: '',
            password: ''
        }
    },
    methods: {
        async submitClick() {
            try {
                const response = await GameAuth.login(this.email, this.password);
                if(!response?.status.status) {
                    console.log('SOMETHING ERROR')
                    return
                }
                console.log(response)
                return navigateTo('/');
            } catch(err) {
                console.log(err)
            }
        }
    }
}
</script>

<style>
body {
    color: white;
    background-color: #1e242e;
}

.form-div {
    height: 100vh;
    margin: 0 auto;
}

.buat-form {
    padding: 3%;
    background-color: rgba(108, 139, 192, 0.15);
}

.question {
    color: white;
}

.linkin {
    color: cornflowerblue;
}
</style>