<template>
    <div class="mb-4 homeheader">
        <div>
            <ForallNavbar/>
        </div>

        <div class=" text-center mt-3">
            <h1>TAPATAN.LTS</h1>
            <h3 class=" pt-3 d-sm-block d-none">PLAY NOW</h3>
            <div class="dropdown d-sm-none">
                <button class="btn btn-primary btn-outline-primary btn-lg dropdown-toggle play-btn" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                    PLAY NOW
                </button>
                <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="dropdownMenuButton1">
                    <li><NuxtLink class="dropdown-item" to="/game/LPVP">Local PVP</NuxtLink></li>
                    <li><NuxtLink class="dropdown-item disabled" to="/game/OPVP">Online PVP</NuxtLink></li>
                    <li><NuxtLink class="dropdown-item" to="/game/PVB">Player VS Bot</NuxtLink></li>
                </ul>
            </div>

            <div class=" container mt-5 d-sm-flex d-none justify-content-center">
                <NuxtLink type="button" class="btn btn-primary btn-lg mx-md-5 mx-auto" to="/game/LPVP">Local PVP</NuxtLink>
                <NuxtLink type="button" class="btn btn-primary btn-lg mx-md-5 mx-auto disabled" to="/game/OPVP">Online PVP</NuxtLink>
                <NuxtLink type="button" class="btn btn-primary btn-lg mx-md-5 mx-auto" to="/game/PVB">Player VS Bot</NuxtLink>
            </div>
        </div>
    </div>
    <body>
        <div class="p-3 text-center">
            Hello World
        </div>
    </body>
    <div>
        <ForallFooter/>
    </div>
</template>

<style>
.homeheader {
    background-image: url('~/assets/img/banner.png');
    background-position: 50%;
    height: 720px;
}
.homeheader h1 {
    margin-top: 9%;
    font-size: 84px;
}
.play-btn {
    color: white;
}

body {
    margin-top: 0;
    color: white;
    background-color: #1e242e;
    min-height: 80vh;
}

@media screen and (max-width: 992px) {
    .homeheader {
        height: 500px;
    }
    .homeheader h1 {
        font-size: 72px;
    }
}

@media screen and (max-width: 768px) {
    .homeheader {
        height: 576px;
    }
    .homeheader h1 {
        font-size: 68px;
    }
}

@media screen and (max-width: 576px) {
    .homeheader {
        height: 480px;
    }
    .homeheader h1 {
        font-size: 56px;
    }
}
</style>