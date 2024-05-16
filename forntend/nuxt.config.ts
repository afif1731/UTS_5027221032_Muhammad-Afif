// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@vesp/nuxt-fontawesome'
  ],
  css: ["bootstrap/scss/bootstrap.scss"],
  fontawesome: {
    icons: {
      brands: ['twitter', 'instagram', 'linkedin', 'github', 'facebook'],
    },
    proIcons: {
      solid: [],
      regular: [],
      light: [],
      thin: [],
      duotone: [],
    },
    sharpIcons: {
      solid: [], 
      regular: [],
      light: [],
      thin: [],
    }
  
  },
  ssr: false,
  vite: {
		resolve: {
			preserveSymlinks: true
		}
	},
  runtimeConfig: {
    public: {
      SERVER_URI: process.env.SERVER_URI
    }
  }
})
