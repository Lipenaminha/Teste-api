<template>
    <div id="app">
        <h1>Teste Vue.js</h1>
        <input v-model="query" placeholder="Digite algo..." />
        <p>Você digitou: {{ query }}</p>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                query: ""
            };
        }
    };
</script>

<style scoped>
    #app {
        text-align: center;
        padding: 20px;
    }

    input {
        padding: 10px;
        font-size: 16px;
        width: 300px;
        margin-top: 20px;
    }
</style>