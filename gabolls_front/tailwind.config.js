import daisyui from 'daisyui';

export default {
    content: ['./src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        extend: {
            colors: {
                primary: '#FF00E6',
                secondary: '#632098',
                tertiary: '#080808',
                quartenary: '#E4DCDC',
                quinary: '#151515'
            }
        },
        fontSize: {
            sm: ['14px', '20px'],
            md: ['16px', '24px'],
            lg: ['20px', '28px'],
            xl: ['24px', '32px'],
            '2xl': ['30px', '40px'],
            '3xl': ['36px', '40px'],
            '4xl': ['48px', '40px'],
            '5xl': ['60px', '40px'],
            '6xl': ['72px', '40px'],
            '7xl': ['96px', '40px'],
            '8xl': ['128px', '40px'],
            '9xl': ['192px', '40px'],
            '10xl': ['256px', '64px']
        }
    },
    plugins: [daisyui],
    daisyui: {
        themes: false
    }
};
