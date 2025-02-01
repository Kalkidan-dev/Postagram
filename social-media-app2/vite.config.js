import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    sourcemap: true, // Ensure sourcemaps are enabled for debugging
  },
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:8000', // Adjust if your API URL differs
    },
  },
  
})
