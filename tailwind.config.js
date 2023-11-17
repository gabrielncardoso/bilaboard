/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/base.html",
    "./static/src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

