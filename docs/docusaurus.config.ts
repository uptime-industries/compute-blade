import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Compute Blade Documentation',
  tagline: 'Bring the Cloud Home',
  favicon: 'img/Favicon.ico',

  // Set the production url of your site here
  url: 'https://docs.computeblade.com/',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'uptime-industries', // Usually your GitHub org/user name.
  projectName: 'compute-blade', // Usually your repo name.
  deploymentBranch: 'main', // The name of the deployment branch.
  trailingSlash: false,

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
          sidebarCollapsible: false,
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
          //   'https://github.com/uptime-industries/compute-blade/tree/main/docs/blog/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/embed-card.webp',
    navbar: {
      // title: 'Home',
      logo: {
        alt: 'compute blade Logo',
        src: 'img/logos/ComputeBlade-logo-black.svg',
        srcDark: 'img/logos/ComputeBlade-logo-green.svg',
        href: '/'
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Blade',
        },
        {
          type: 'docSidebar',
          sidebarId: 'fanSidebar',
          position: 'left',
          label: 'Fan Unit',
        },
        {
          type: 'docSidebar',
          sidebarId: 'runnerSidebar',
          position: 'left',
          label: 'BladeRunner',
        },
        // {
        //   type: 'docSidebar',
        //   sidebarId: 'guideSidebar',
        //   position: 'left',
        //   label: 'Guides',
        // },
        {
          to: 'timeline',
          label: 'Timeline',
          position: 'right'
        },

        {to: '/blog', label: 'Blog', position: 'right'},
        {
          href: 'https://computeblade.com',
          position: 'right',
          className: 'header-website-link',
          'aria-label': 'Website link'
        },
        {
          href: 'https://discord.gg/invite/uptime-industries-952334175501946902',
          position:'right',
          className: 'header-discord-link',
          'aria-label': 'Discord Invite'
        },
        {
          href: 'https://github.com/uptime-industries/compute-blade',
          // label: 'GitHub',
          position: 'right',
          className: 'header-github-link',
          'aria-label': 'GitHub repository'
        },

      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Compute Blade',
              to: 'blade',
            },
            {
              label: 'Getting Started with Compute Blade',
              to: 'blade/getting-started/assembly'
            },
            {
              label: 'Fan Unit',
              to: 'fan-unit'
            },
            {
              label: 'BladeRunner',
              to: 'bladerunner'
            },
            {
              label: 'Data Sheet',
              to: 'datasheets'
            }
          ],
        },
        {
          title: 'Social',
          items: [
            {
              label: 'LinkedIn',
              href: 'https://www.linkedin.com/company/uptimeindustries',
            },
            {
              label: 'Instagram',
              href: 'https://www.instagram.com/uptime.lab/',
            },
            {
              label: 'Bluesky',
              href: 'https://bsky.app/profile/uptime.industries',
            },
            {
              label: 'Discord',
              href: 'https://discord.gg/invite/uptime-industries-952334175501946902',
            }
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
              href: 'https://uptime.industries/',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/uptime-industries/',
            },
            {
              label: 'Legal',
              href: 'https://computeblade.com/privacy-policy/'
            }
          ],
        },
        {
          title: 'Contact',
          items: [
            {
              html:`<p>Uptime Industries Inc.
                  447 Broadway #2114
                  New York, NY 10013
                  United States
                </p>`,
            },
            {
              html: '<p>info@uptime.industries</p>',
            },
            {
              html: '<p>+1 (315) 784-7820</p>'
            }
          ]
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Uptime Industries. Built with Docusaurus.`,
      logo: {
        src: 'img/logos/UptimeIndustries-logo-white.svg',
        srcDark: 'img/logos/UptimeIndustries-logo-green.svg',
        height: 100
      },

    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'c', 'powershell', 'rust']
    },
    algolia: {
      // The application ID provided by Algolia
      appId: 'PSGE3SK6B9',

      // Public API key: it is safe to commit it
      apiKey: '8f39658a11cfdb405dd6f4e805831bac',

      indexName: 'computeblade',

      // Optional: see doc section below
      contextualSearch: true,

      // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
      // externalUrlRegex: 'external\\.com|domain\\.com',

      // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
      // replaceSearchResultPathname: {
      //   from: '/docs/', // or as RegExp: /\/docs\//
      //   to: '/',
      // },

      // Optional: Algolia search parameters
      // searchParameters: {},

      // Optional: path for search page that enabled by default (`false` to disable it)
      // searchPagePath: 'search',

      // Optional: whether the insights feature is enabled or not on Docsearch (`false` by default)
      // insights: false,

      //... other Algolia params
    },
    docs:{
      sidebar: {
        autoCollapseCategories: false
      }
    },
  } satisfies Preset.ThemeConfig,

  plugins: [
    [      
      '@docusaurus/plugin-client-redirects',
      {
        redirects: [
          {
            to: '/datasheets/',
            from: ['/data-sheets/'],
          },
          {
            to: '/blade/getting-started/assembly/',
            from: ['/getting-started/']
          },
        ],
      },
    ],
    [
      './hubspot',
      {
        accountId: 47862563,
      }
    ]
  ]
};

export default config;
