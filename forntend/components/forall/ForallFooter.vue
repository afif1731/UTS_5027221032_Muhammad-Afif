<template>
    <footer class="text-center bg-body-tertiary">
        <div style="background-color: #0a4275;">
            <!-- Grid container -->
            <div class="container pt-4">
                <!-- Section: Social media -->
                <section class="mb-4">
                <!-- Facebook -->
                <a
                    data-mdb-ripple-init
                    class="btn btn-link btn-floating btn-lg text-body m-1"
                    href="https://facebook.com/m.afifraihan/"
                    target="_blank"
                    role="button"
                    data-mdb-ripple-color="dark"
                    >
                    <font-awesome :icon="['fab', 'facebook']" style="font-size: 36px; " :style="{color: 'white'}" />
                </a>

                <!-- Instagram -->
                <a
                    data-mdb-ripple-init
                    class="btn btn-link btn-floating btn-lg text-body m-1"
                    href="https://www.instagram.com/_fif.17/"
                    target="_blank"
                    role="button"
                    data-mdb-ripple-color="dark"
                    >
                    <font-awesome :icon="['fab', 'instagram']" style="font-size: 36px; " :style="{color: 'white'}" />
                </a>
                

                <!-- Linkedin -->
                <a
                    data-mdb-ripple-init
                    class="btn btn-link btn-floating btn-lg text-body m-1"
                    href="https://www.linkedin.com/in/afif-muhammad-473818248/"
                    target="_blank"
                    role="button"
                    data-mdb-ripple-color="dark"
                    >
                    <font-awesome :icon="['fab', 'linkedin']" style="font-size: 36px; " :style="{color: 'white'}" />
                </a>

                <!-- Github -->
                <a
                    data-mdb-ripple-init
                    class="btn btn-link btn-floating btn-lg m-1"
                    href="https://github.com/afif1731"
                    target="_blank"
                    role="button"
                    data-mdb-ripple-color="dark"
                    >
                    <font-awesome :icon="['fab', 'github']" style="font-size: 36px; " :style="{color: 'white'}" />
                </a>
                </section>
                <!-- Section: Social media -->
            </div>
            <!-- Grid container -->

            <!-- Copyright -->
            <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
                ® 2024 Muhammad Afif - System Integration Mini Project Assignment
            </div>
            <!-- Copyright -->
        </div>
    </footer>
</template>
