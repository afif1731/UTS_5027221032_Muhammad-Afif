<template>
    <header>
        <ForallNavbar/>
    </header>

    <body class="mx-1 mx-ms-3 mt-3">
        <GamecompBoard game-type="LPVP" />
    </body>

    <footer>
        <ForallFooter/>
    </footer>
</template>

<style>
body {
    margin-top: 0;
    color: white;
    background-color: #1e242e;
    min-height: 80vh;
}

@media screen and (max-width: 576px) {
    body {
        min-height: 60vh;
    }  
}
</style>