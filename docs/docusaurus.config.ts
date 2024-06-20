import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Compute Blade Documentation',
  tagline: 'Bring the Cloud Home',
  favicon: 'img/Favicon.ico',

  // Set the production url of your site here
  url: 'https://uptime-industries.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/compute-blade/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'uptime-industries', // Usually your GitHub org/user name.
  projectName: 'compute-blade', // Usually your repo name.
  deploymentBranch: 'main', // The name of the deployment branch.
  trailingSlash: true,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
    path: 'i18n',
    localeConfigs: {
      en: {
        label: 'English',
        direction: 'ltr',
        htmlLang: 'en-US',
        calendar: 'gregory',
        path: 'en',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/uptime-industries/compute-blade/tree/main/docs/',
        },
        blog: {
          showReadingTime: true,
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/uptime-industries/compute-blade/tree/main/blog/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/embed-card.png',
    navbar: {
      // title: 'Home',
      logo: {
        alt: 'compute blade Logo',
        src: 'img/ComputeBlade-logo-black.svg',
        srcDark: 'img/ComputeBlade-logo-green.svg'
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Docs',
        },
        // {
        //   type: 'docSidebar',
        //   sidebarId: 'guidesSidebar',
        //   position: 'left',
        //   label: 'Guides',
        // },
        // {to: '/blog', label: 'Blog', position: 'left'},
        {
          label: 'Website',
          href: 'https://computeblade.com',
          position: 'right'
        },
        {
          href: 'https://github.com/uptime-industries/compute-blade',
          label: 'GitHub',
          position: 'right',
        },
        
      ],
    },
    footer: {
      style: 'dark',
      links: [
        // {
        //   title: 'Docs',
        //   items: [
        //     {
        //       label: 'Tutorial',
        //       to: '/docs/intro',
        //     },
        //   ],
        // },
        {
          title: 'Community',
          items: [
            {
              label: 'LinkedIn',
              href: 'https://www.linkedin.com/company/uptimeindustries',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/uptime-industries',
            }
          ],
        },
        {
          title: 'Social',
          items: [
            {
              label: 'Instagram',
              href: 'https://www.instagram.com/uptime.lab/',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/Merocle',
            },
          ],
        },
        {
          title: 'More',
          items: [
            // {
            //   label: 'Blog',
            //   to: '/blog',
            // },
            {
              label: 'Website',
              href: 'https://computeblade.com',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/uptime-industries',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Uptime Industries. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'c', 'powershell']
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
