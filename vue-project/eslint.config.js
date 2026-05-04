import js from '@eslint/js'
import skipFormatting from '@vue/eslint-config-prettier/skip-formatting'
import pluginVue from 'eslint-plugin-vue'
import { defineConfig, globalIgnores } from 'eslint/config'
import globals from 'globals'

export default defineConfig([
  globalIgnores(['**/dist/**', '**/dist-ssr/**', '**/coverage/**']),

  // General JS and Vue config
  {
    name: 'app/main-config',
    files: ['**/*.{js,vue}'],
    languageOptions: {
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      'vue/block-order': [
        'error',
        {
          order: ['script', 'template', 'style'],
        },
      ],
      'vue/padding-line-between-blocks': ['error', 'always'],
    },
  },

  // Base recommended configs
  js.configs.recommended,
  ...pluginVue.configs['flat/essential'],
  skipFormatting,

  // Specific overrides
  {
    name: 'app/pages-overrides',
    files: ['src/pages/**/*.vue'],
    rules: {
      'vue/multi-word-component-names': 'off',
    },
  },
])
