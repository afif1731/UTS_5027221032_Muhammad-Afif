<template>
    <nav class="navbar navbar-expand-lg navbar-dark mx-3 mb-16 rounded-3" style="background-color:#2a3843;">
        <div class="container-fluid d-flex">
            <NuxtLink class="navbar-brand position-absolute h-100 d-inline-block align-baseline mt-3" to="/">TAPATAN.LTS</NuxtLink>

            <button class="navbar-toggler ms-auto" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse d-lg-flex justify-content-end" id="navbarNavDropdown">
            <ul class="navbar-nav d-flex justify-content-center">
                <li class="nav-item dropdown mx-lg-4">
                    <NuxtLink class="nav-link dropdown-toggle active" id="navbarScrollingDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" to="#">Play</NuxtLink>
                    
                    <ul class="dropdown-menu dropdown-menu-dark w-25" aria-labelledby="navbarScrollingDropdown">
                        <li><NuxtLink class="dropdown-item" to="/game/LPVP">Local PVP</NuxtLink></li>
                        <li><NuxtLink class="dropdown-item disabled" to="/game/OPVP">Online PVP</NuxtLink></li>
                        <li><NuxtLink class="dropdown-item" to="/game/PVB">Player VS Bot</NuxtLink></li>
                    </ul>
                </li>
                <li class="nav-item mx-lg-3">
                    <NuxtLink class="nav-link active" aria-current="page" to="/tutorial">Tutorial</NuxtLink>
                </li>
                <li class="nav-item mx-lg-3">
                    <NuxtLink class="nav-link active" aria-current="page" to="/#about">About</NuxtLink>
                </li>
                <li class="nav-item float-lg-end mx-lg-3">
                    <NuxtLink class="nav-link active" aria-current="page" to="/login">Login</NuxtLink>
                </li>
            </ul>
            </div>
        </div>
    </nav>
</template>