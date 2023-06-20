/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic':
          'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
      },
    },
    colors: {
      // For primary
      'primary': '#5fd4fd',
      'on-primary': '#003544',
      'primary-container': '#004d62',
      'on-primary-container': '#baeaff',

      // For secondary
      'secondary': '#b3cad5',
      'on-secondary': '#1e333c',
      'secondary-container': '#354a53',
      'on-secondary-container': '#cfe6f1',

      // For Tertiary
      'tertiary': '#c4c3eb',
      'on-tertiary': '#2d2d4d',
      'tertiary-container': '#434465',
      'on-tertiary-container': '#e1dfff',

      // For error
      'error': '#ffb4ab',
      'on-error': '#690005',
      'error-container': '#93000a',
      'on-error-container': '#ffdad6',

      // For background
      'background': '#191c1d',
      'on-background': '#e1e3e4',

      'outline': '#8a9296',

    },
  },
  plugins: [],
}
